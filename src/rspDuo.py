from ctypes import Structure, c_int, c_ubyte

# Constant Definitions
RSPDUO_NUM_LNA_STATES = 10
RSPDUO_NUM_LNA_STATES_AMPORT = 5
RSPDUO_NUM_LNA_STATES_AM = 7
RSPDUO_NUM_LNA_STATES_LBAND = 9


# Enumerated Data Types
class sdrplay_api_RspDuoModeT(c_int):
    sdrplay_api_RspDuoMode_AUNKNOWN = 0
    sdrplay_api_RspDuoMode_ASINGLE_TUNER = 1
    sdrplay_api_RspDuoMode_ADUAL_TUNER = 2
    sdrplay_api_RspDuoMode_AMASTER = 4
    sdrplay_api_RspDuoMode_ASLAVE = 8

class sdrplay_api_RspDuoAmPortSelectT(c_int):
    sdrplay_api_RspDuo_AAMPORT_1 = 1
    sdrplay_api_RspDuo_AAMPORT_2 = 0



# Data Structures
class sdrplay_api_RspDuoParamsT(Structure):
    _fields_ = [
        ("extRefOutputEn", c_int),  # default: 0
    ]

class sdrplay_api_RspDuoResetSlaveFlagsT(Structure):
    _fields_ = [
        ("resetGainUpdate", c_ubyte),  # default: 0
        ("resetRfUpdate", c_ubyte),  # default: 0
    ]

class sdrplay_api_RspDuoTunerParamsT(Structure):
    _fields_ = [
        ("biasTEnable", c_ubyte),  # default: 0
        ("tuner1AmPortSel", sdrplay_api_RspDuoAmPortSelectT),  # default: RspDuoAmPortSelectT.AMPORT_2
        ("tuner1AmNotchEnable", c_ubyte),  # default: 0
        ("rfNotchEnable", c_ubyte),  # default: 0
        ("rfDabNotchEnable", c_ubyte),  # default: 0
        ("resetSlaveFlags", sdrplay_api_RspDuoResetSlaveFlagsT),
    ]
