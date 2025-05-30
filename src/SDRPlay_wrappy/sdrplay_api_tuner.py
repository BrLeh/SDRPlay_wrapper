import ctypes

# Enumerated Data Types
class sdrplay_api_Bw_MHzT(ctypes.c_uint):
    sdrplay_api_BW_Undefined = 0
    sdrplay_api_BW_0_200 = 200
    sdrplay_api_BW_0_300 = 300
    sdrplay_api_BW_0_600 = 600
    sdrplay_api_BW_1_536 = 1536
    sdrplay_api_BW_5_000 = 5000
    sdrplay_api_BW_6_000 = 6000
    sdrplay_api_BW_7_000 = 7000
    sdrplay_api_BW_8_000 = 8000

class sdrplay_api_If_kHzT(ctypes.c_int):
    sdrplay_api_IF_Undefined = -1
    sdrplay_api_IF_Zero = 0
    sdrplay_api_IF_0_450 = 450
    sdrplay_api_IF_1_620 = 1620
    sdrplay_api_IF_2_048 = 2048

class sdrplay_api_LoModeT(ctypes.c_uint):
    sdrplay_api_LO_Undefined = 0
    sdrplay_api_LO_Auto = 1
    sdrplay_api_LO_120MHz = 2
    sdrplay_api_LO_144MHz = 3
    sdrplay_api_LO_168MHz = 4

class sdrplay_api_MinGainReductionT(ctypes.c_uint):
    sdrplay_api_EXTENDED_MIN_GR = 0
    sdrplay_api_NORMAL_MIN_GR = 20

class sdrplay_api_TunerSelectT(ctypes.c_uint):
    sdrplay_api_Neither = 0
    sdrplay_api_Tuner_A = 1
    sdrplay_api_Tuner_B = 2
    sdrplay_api_Tuner_Both = 3


class sdrplay_api_GainValuesT(ctypes.Structure):
    _fields_ = [
        ("curr", ctypes.c_float),  
        ("max", ctypes.c_float),  
        ("min", ctypes.c_float)   
    ]
class sdrplay_api_GainT(ctypes.Structure):
    _fields_ = [
        ("gRdB", ctypes.c_int),  # Gain reduction in dB
        ("LNAstate", ctypes.c_uint),  # LNA status
        ("syncUpdate", ctypes.c_ubyte), 
        ("minGr", sdrplay_api_MinGainReductionT),  
        ("gainVals", sdrplay_api_GainValuesT)  
    ]

class sdrplay_api_RfFreqT(ctypes.Structure):
    _fields_ = [
        ("rfHz", ctypes.c_double), 
        ("syncUpdate", ctypes.c_ubyte)  
    ]

class sdrplay_api_DcOffsetTunerT(ctypes.Structure):
    _fields_ = [
        ("dcCal", ctypes.c_ubyte),  
        ("speedUp", ctypes.c_ubyte),  
        ("trackTime", ctypes.c_int),  
        ("refreshRateTime", ctypes.c_int) 
    ]

class sdrplay_api_TunerParamsT(ctypes.Structure):
    _fields_ = [
        ("bwType", sdrplay_api_Bw_MHzT), 
        ("ifType", sdrplay_api_If_kHzT),
        ("loMode", sdrplay_api_LoModeT), 
        ("gain", sdrplay_api_GainT),  
        ("rfFreq", sdrplay_api_RfFreqT), 
        ("dcOffsetTuner", sdrplay_api_DcOffsetTunerT)
    ]