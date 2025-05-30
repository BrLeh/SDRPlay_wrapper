import ctypes

# Constant Definitions
RSPII_NUM_LNA_STATES = 9
RSPII_NUM_LNA_STATES_AMPORT = 5
RSPII_NUM_LNA_STATES_420MHZ = 6

class sdrsplay_api_Rsp2AntennaSelectT(ctypes.c_int):
    sdrplay_api_Rsp2_ANTENNA_A = 5
    sdrplay_api_Rsp2_ANTENNA_B = 6

class sdrsplay_api_Rsp2AmPortSelectT(ctypes.c_int):
    sdrplay_api_Rsp2_AMPORT_1 = 1
    sdrplay_api_Rsp2_AMPORT_2 = 0



class sdrplay_api_Rsp2ParamsT(ctypes.Structure):
    _fields_ = [
        ("extRefOutputEn", ctypes.c_ubyte),  # default: 0
    ]

class sdrplay_api_Rsp2TunerParamsT(ctypes.Structure):
    _fields_ = [
        ("biasTEnable", ctypes.c_ubyte),  # default: 0
        ("amPortSel", sdrsplay_api_Rsp2AmPortSelectT),  # default: Rsp2AmPortSelectT.AMPORT_2
        ("antennaSel", sdrsplay_api_Rsp2AntennaSelectT),  # default: Rsp2AntennaSelectT.ANTENNA_A
        ("rfNotchEnable", ctypes.c_ubyte),  # default: 0
    ]
