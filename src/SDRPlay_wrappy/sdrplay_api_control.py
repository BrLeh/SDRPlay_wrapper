from ctypes import Structure, c_ubyte, c_int, c_ushort

# Enumerated Data Types
class sdrplay_api_AgcControlT(c_int):
    sdrplay_api_AGC_DISABLE = 0
    sdrplay_api_AGC_100HZ = 1
    sdrplay_api_AGC_50HZ = 2
    sdrplay_api_AGC_5HZ = 3
    sdrplay_api_AGC_CTRL_EN = 4

class sdrplay_api_AdsbModeT(c_int):
    sdrplay_api_ADSB_DECIMATION = 0
    sdrplay_api_ADSB_NO_DECIMATION_LOWPASS = 1
    sdrplay_api_ADSB_NO_DECIMATION_BANDPASS_2MHZ = 2
    sdrplay_api_ADSB_NO_DECIMATION_BANDPASS_3MHZ = 3



# Data Structures
class sdrplay_api_DcOffsetT(Structure):
    _fields_ = [
        ("DCenable", c_ubyte),  # default: 1
        ("IQenable", c_ubyte),  # default: 1
    ]

class sdrplay_api_DecimationT(Structure):
    _fields_ = [
        ("enable", c_ubyte),  # default: 0
        ("decimationFactor", c_ubyte),  # default: 1
        ("wideBandSignal", c_ubyte),  # default: 0
    ]

class sdrplay_api_AgcT(Structure):
    _fields_ = [
        ("enable", sdrplay_api_AgcControlT),  # default: AgcControlT.AGC_50HZ
        ("setPoint_dBfs", c_int),  # default: -60
        ("attack_ms", c_ushort),  # default: 0
        ("decay_ms", c_ushort),  # default: 0
        ("decay_delay_ms", c_ushort),  # default: 0
        ("decay_threshold_dB", c_ushort),  # default: 0
        ("syncUpdate", c_int),  # default: 0
    ]

class sdrplay_api_ControlParamsT(Structure):
    _fields_ = [
        ("dcOffset", sdrplay_api_DcOffsetT),
        ("decimation", sdrplay_api_DecimationT),
        ("agc", sdrplay_api_AgcT),
        ("adsbMode", sdrplay_api_AdsbModeT),  # default: AdsbModeT.ADSB_DECIMATION
    ]
