import ctypes
from .sdrplay_api_tuner import *
from .sdrplay_api_control import *
from .rspdx import *
from .rsp1a import *
from .rsp2a import *
from .rspDuo import *

class sdrplay_api_RxChannelParamsT(ctypes.Structure):
    _fields_ = [
        ("tunerParams", sdrplay_api_TunerParamsT),  # Paramètres du tuner
        ("ctrlParams", sdrplay_api_ControlParamsT),  # Contrôles divers
        ("rsp1aTunerParams", sdrplay_api_Rsp1aTunerParamsT),
        ("rsp2TunerParams", sdrplay_api_Rsp2TunerParamsT),
        ("rspDuoTunerParams", sdrplay_api_RspDuoTunerParamsT),
        ("rspDxTunerParams", sdrplay_api_RspDxTunerParamsT)
    ]