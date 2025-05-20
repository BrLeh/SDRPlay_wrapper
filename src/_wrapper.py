import ctypes
import time
import numpy as np
import sys
import os
import queue
import threading
import signal


from rspdx import *
from rsp1a import *
from rsp2a import *
from rspDuo import *
from sdrplay_api_control import *
from sdrplay_api import *
from sdrplay_api_dev import *
from sdrplay_api_tuner import *
from sdrplay_api_callback import *
from sdrplay_api_rx_channel import *



if sys.platform == "win32":
    libname = "yourlib.dll"
    raise ImportError("TO DO")
else:
    libname = "libsdrplay_api.so"

lib_path = os.path.join(os.path.dirname(__file__), "lib", libname)
sdrplay_api = ctypes.CDLL(lib_path)  # Linux

class SDRStreamHandler:
    def __init__(self, sdrplay_api, device_handle, cbFns):
        self.api = sdrplay_api
        self.dev = ctypes.c_void_p(device_handle.contents.dev)
        self.cbFns = cbFns

        self.queue = queue.Queue(maxsize=100)
        self.running = False
        self.consumer_thread = None

        # Crée le callback C->Python (important de le garder en référence)
        self._callback_c = self._build_callback()
        self.cbFns.StreamACbFn = self._callback_c

    def _build_callback(self):
        StreamACallbackType = ctypes.CFUNCTYPE(
            None,
            ctypes.POINTER(ctypes.c_short),
            ctypes.POINTER(ctypes.c_short),
            ctypes.POINTER(sdrplay_api_StreamCbParamsT),
            ctypes.c_uint,
            ctypes.c_uint,
            ctypes.c_void_p  # cbContext
            
        )
        StreamBCallbackType = ctypes.CFUNCTYPE(
            None,
            ctypes.POINTER(ctypes.c_short), 
            ctypes.POINTER(ctypes.c_short),
            ctypes.POINTER(sdrplay_api_StreamCbParamsT), 
            ctypes.c_uint,  # numSamples
            ctypes.c_uint,  # reset
            ctypes.c_void_p  # cbContext
        )
        EventCallbackType = ctypes.CFUNCTYPE(
            None,  # 'void`
            sdrplay_api_EventT,  # eventId
            sdrplay_api_TunerSelectT,  # tuner
            ctypes.POINTER(sdrplay_api_EventParamsT),  # params
            ctypes.c_void_p  # cbContext
        )

        def StreamACallback(xi, xq, params, numSamples, reset, cbContext=ctypes.c_void_p()):
            if reset:
                print(f"[Callback] Reset reçu, numSamples={numSamples}")
                return

            np_xi = np.ctypeslib.as_array(xi, shape=(numSamples,))
            np_xq = np.ctypeslib.as_array(xq, shape=(numSamples,))
            iq_samples = (np_xi.astype(np.float32) + 1j * np_xq.astype(np.float32)).astype(np.complex64)/ 32768.0

            try:
                self.queue.put_nowait(iq_samples)
            except queue.Full:
                print("[Callback] Queue pleine : bloc ignoré")

        return StreamACallbackType(StreamACallback)

    def _consumer_loop(self):
        print("[Thread] Consommateur IQ démarré")
        while self.running:
            try:
                iq_samples = self.queue.get(timeout=1)
                self.handle_samples(iq_samples)
            except queue.Empty:
                continue

    def handle_samples(self, iq_samples):
        # Traitement à adapter selon ton usage (FFT, enregistrement, etc.)
        power = np.mean(np.abs(iq_samples)**2)
        print(f"[Thread] Bloc reçu, puissance moyenne : {power:.2f}")

    def start(self):
        print("[SDR] Initialisation...")
        self.running = True
        self.consumer_thread = threading.Thread(target=self._consumer_loop)
        self.consumer_thread.start()

        ret = self.api.sdrplay_api_Init(self.dev, ctypes.byref(self.cbFns), ctypes.c_void_p())
        if ret != 0:
            raise RuntimeError(f"Erreur lors de l'initialisation SDRPlay: code {ret}")
        print("[SDR] Capture démarrée")

    def stop(self):
        print("[SDR] Arrêt...")
        self.running = False
        self.api.sdrplay_api_Uninit(self.dev)
        self.consumer_thread.join()
        print("[SDR] Arrêt complet")

    def register_signal_handler(self):
        def handler(sig, frame):
            print("\n[Signal] Ctrl+C détecté, arrêt propre...")
            self.stop()
        signal.signal(signal.SIGINT, handler)
        





