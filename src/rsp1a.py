import ctypes

# Constant Definitions
RSPIA_NUM_LNA_STATES = 10  # Number of LNA states in all bands (except where defined differently below)
RSPIA_NUM_LNA_STATES_AM = 7  # Number of LNA states in AM band
RSPIA_NUM_LNA_STATES_LBAND = 9  # Number of LNA states in L band

# RSP1A RF Notch Control Parameters Structure
class sdrplay_api_Rsp1aParamsT(ctypes.Structure):
    _fields_ = [
        ("rfNotchEnable", ctypes.c_ubyte),  # default: 0
        ("rfDabNotchEnable", ctypes.c_ubyte)  # default: 0
    ]

# RSP1A Bias-T Control Parameters Structure
class sdrplay_api_Rsp1aTunerParamsT(ctypes.Structure):
    _fields_ = [
        ("biasTEnable", ctypes.c_ubyte)  # default: 0
    ]