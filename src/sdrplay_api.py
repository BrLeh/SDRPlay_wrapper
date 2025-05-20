import ctypes
from sdrplay_api_tuner import *
from sdrplay_api_dev import *
from sdrplay_api_rx_channel import *
from rspdx import *
from rsp1a import *
from rsp2a import *
from rspDuo import *

SDRPLAY_MAX_SER_NO_LEN = 64  # Taille max du numéro de série

class sdrplay_api_DbgLvl_t(ctypes.c_uint):
    sdrplay_api_DbgLvl_Disable = 0,
    sdrplay_api_DbgLvl_Verbose = 1,
    sdrplay_api_DbgLvl_Warning = 2,
    sdrplay_api_DbgLvl_Error = 3,
    sdrplay_api_DbgLvl_Message = 4

class sdrplay_api_DeviceT(ctypes.Structure):
    _fields_ = [
        ("SerNo", ctypes.c_char * SDRPLAY_MAX_SER_NO_LEN),  # Numéro de série
        ("hwVer", ctypes.c_ubyte),  # Version matérielle
        ("tuner", sdrplay_api_TunerSelectT),  # Tuner disponible
        ("rspDuoMode", sdrplay_api_RspDuoModeT),  # Mode RSPduo (non utilisé pour RSPdx)
        ("valid", ctypes.c_ubyte),  # Indicateur de disponibilité
        ("rspDuoSampleFreq", ctypes.c_double),  # Fréquence d'échantillonnage (pour RSPduo)
        ("dev", ctypes.c_void_p)  # Handle du périphérique après sélection
    ]

class sdrplay_api_DeviceParamsT(ctypes.Structure):
    _fields_ = [
        ("devParams", ctypes.POINTER(sdrplay_api_DevParamsT)),  # Paramètres généraux
        ("rxChannelA", ctypes.POINTER(sdrplay_api_RxChannelParamsT)),  # Tuner A
        ("rxChannelB", ctypes.POINTER(sdrplay_api_RxChannelParamsT))   # Tuner B (RSPduo)
    ]