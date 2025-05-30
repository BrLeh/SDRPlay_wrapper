import ctypes

# Constant Definitions
RSPDX_NUM_LNA_STATES = 28
RSPDX_NUM_LNA_STATES_AMPORT2_0_12 = 19
RSPDX_NUM_LNA_STATES_AMPORT2_12_50 = 20
RSPDX_NUM_LNA_STATES_AMPORT2_50_60 = 25
RSPDX_NUM_LNA_STATES_VHF_BAND3 = 27
RSPDX_NUM_LNA_STATES_420MHZ = 21
RSPDX_NUM_LNA_STATES_LBAND = 19
RSPDX_NUM_LNA_STATES_DX = 22

class sdrplay_api_RspDx_AntennaSelectT(ctypes.c_uint):
    sdrplay_api_RspDx_ANTENNA_A = 0
    sdrplay_api_RspDx_ANTENNA_B = 1
    sdrplay_api_RspDx_ANTENNA_C = 2

class sdrplay_api_RspDx_HdrModeBwT(ctypes.c_uint):
    sdrplay_api_RspDx_HDRMODE_BW_0_200 = 0
    sdrplay_api_RspDx_HDRMODE_BW_0_500 = 1
    sdrplay_api_RspDx_HDRMODE_BW_1_200 = 2
    sdrplay_api_RspDx_HDRMODE_BW_1_700 = 3

class sdrplay_api_RspDxParamsT(ctypes.Structure):
    _fields_ = [
        ("hdrEnable", ctypes.c_ubyte),       # Enable HDR
        ("biasTEnable", ctypes.c_ubyte),     # Enable Bias-T
        ("antennaSel", sdrplay_api_RspDx_AntennaSelectT), # Antenna selection
        ("rfNotchEnable", ctypes.c_ubyte),   # Notch Filter RF
        ("rfDabNotchEnable", ctypes.c_ubyte) # Notch Filter DAB
    ]

class sdrplay_api_RspDxTunerParamsT(ctypes.Structure):
    fields_ = [
            ("hdrBw", sdrplay_api_RspDx_HdrModeBwT)  # HDR band selection
        ]