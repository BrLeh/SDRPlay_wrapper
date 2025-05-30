import ctypes
from .sdrplay_api_tuner import *
from .sdrplay_api_dev import *
from .sdrplay_api_rx_channel import *
from .rspdx import *
from .rsp1a import *
from .rsp2a import *
from .rspDuo import *

SDRPLAY_MAX_SER_NO_LEN = 64  

class sdrplay_api_DbgLvl_t(ctypes.c_uint):
    sdrplay_api_DbgLvl_Disable = 0,
    sdrplay_api_DbgLvl_Verbose = 1,
    sdrplay_api_DbgLvl_Warning = 2,
    sdrplay_api_DbgLvl_Error = 3,
    sdrplay_api_DbgLvl_Message = 4

class sdrplay_api_DeviceT(ctypes.Structure):
    _fields_ = [
        ("SerNo", ctypes.c_char * SDRPLAY_MAX_SER_NO_LEN), 
        ("hwVer", ctypes.c_ubyte),  
        ("tuner", sdrplay_api_TunerSelectT),  
        ("rspDuoMode", sdrplay_api_RspDuoModeT),  
        ("valid", ctypes.c_ubyte), 
        ("rspDuoSampleFreq", ctypes.c_double), 
        ("dev", ctypes.c_void_p) 
    ]

class sdrplay_api_DeviceParamsT(ctypes.Structure):
    _fields_ = [
        ("devParams", ctypes.POINTER(sdrplay_api_DevParamsT)),  
        ("rxChannelA", ctypes.POINTER(sdrplay_api_RxChannelParamsT)),  
        ("rxChannelB", ctypes.POINTER(sdrplay_api_RxChannelParamsT)) 
    ]