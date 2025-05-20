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
        ("curr", ctypes.c_float),  # Gain actuel
        ("max", ctypes.c_float),   # Gain max
        ("min", ctypes.c_float)    # Gain min
    ]
class sdrplay_api_GainT(ctypes.Structure):
    _fields_ = [
        ("gRdB", ctypes.c_int),  # Gain reduction en dB
        ("LNAstate", ctypes.c_uint),  # État du LNA (pré-ampli)
        ("syncUpdate", ctypes.c_ubyte),  # Mise à jour synchronisée
        ("minGr", sdrplay_api_MinGainReductionT),  # Gain minimum
        ("gainVals", sdrplay_api_GainValuesT)  # Structure avec les valeurs de gain
    ]

class sdrplay_api_RfFreqT(ctypes.Structure):
    _fields_ = [
        ("rfHz", ctypes.c_double),  # Fréquence RF en Hz
        ("syncUpdate", ctypes.c_ubyte)  # Mise à jour synchronisée
    ]

class sdrplay_api_DcOffsetTunerT(ctypes.Structure):
    _fields_ = [
        ("dcCal", ctypes.c_ubyte),  # Mode de calibration
        ("speedUp", ctypes.c_ubyte),  # Accélération de calibration
        ("trackTime", ctypes.c_int),  # Temps de suivi
        ("refreshRateTime", ctypes.c_int)  # Taux de rafraîchissement
    ]

class sdrplay_api_TunerParamsT(ctypes.Structure):
    _fields_ = [
        ("bwType", sdrplay_api_Bw_MHzT),  # Type de bande passante
        ("ifType", sdrplay_api_If_kHzT),  # Type de fréquence intermédiaire
        ("loMode", sdrplay_api_LoModeT),  # Mode de l'oscillateur local
        ("gain", sdrplay_api_GainT),  # Paramètres de gain
        ("rfFreq", sdrplay_api_RfFreqT),  # Fréquence RF
        ("dcOffsetTuner", sdrplay_api_DcOffsetTunerT)  # Calibration DC
    ]