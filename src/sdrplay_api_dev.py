import ctypes
from rspdx import *
from rsp1a import *
from rsp2a import *
from rspDuo import *

class sdrplay_api_TransferModeT(ctypes.c_uint):
    sdrplay_api_ISOCH = 0  # Mode isochrone (priorité aux flux en temps réel)
    sdrplay_api_BULK = 1   # Mode bulk (priorité à la fiabilité du transfert)

class sdrplay_api_FsFreqT(ctypes.Structure):
    _fields_ = [("fsHz", ctypes.c_double),
                ("syncUpdate", ctypes.c_ubyte),
                ("reCal", ctypes.c_ubyte)]
    
class sdrplay_api_SyncUpdateT(ctypes.Structure):
    _fields_ = [("sampleNum", ctypes.c_uint),
                ("period", ctypes.c_uint)]
    
class sdrplay_api_ResetFlagsT(ctypes.Structure):
    _fields_ = [("resetGainUpdate", ctypes.c_ubyte),
                ("resetRfUpdate", ctypes.c_ubyte),
                ("resetFsUpdate", ctypes.c_ubyte)]
    

class sdrplay_api_DevParamsT(ctypes.Structure):
    _fields_ = [("ppm", ctypes.c_double),
                ("fsFreq", sdrplay_api_FsFreqT),
                ("syncUpdate", sdrplay_api_SyncUpdateT),
                ("resetFlags", sdrplay_api_ResetFlagsT),
                ("mode", sdrplay_api_TransferModeT),
                ("samplesPerPkt", ctypes.c_uint),
                ("rsp1Params",sdrplay_api_Rsp1aParamsT),
                ("rsp2Params",sdrplay_api_Rsp2ParamsT),
                ("rspDuoParams",sdrplay_api_RspDuoParamsT),
                ("rspDxParams", sdrplay_api_RspDxParamsT)]  