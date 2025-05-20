from ctypes import CFUNCTYPE, POINTER, c_short, Structure, Union, c_uint, c_int, c_double, c_void_p
from sdrplay_api_tuner import sdrplay_api_TunerSelectT


# Enumerated Data Types
class sdrplay_api_PowerOverloadCbEventIdT(c_uint):
    sdrplay_api_OVERLOAD_DETECTED = 0
    sdrplay_api_OVERLOAD_CORRECTED = 1

class sdrplay_api_RspDuoModeCbEventIdT(c_uint):
    sdrplay_api_MASTER_INITIALISED = 0
    sdrplay_api_SLAVE_ATTACHED = 1
    sdrplay_api_SLAVE_DETACHED = 2
    sdrplay_api_SLAVE_INITIALISED = 3
    sdrplay_api_SLAVE_UNINITIALISED = 4
    sdrplay_api_MASTER_DLL_DISAPPEARED = 5
    sdrplay_api_SLAVE_DLL_DISAPPEARED = 6

class sdrplay_api_EventT(c_uint):
    sdrplay_api_GAIN_CHANGE = 0
    sdrplay_api_POWER_OVERLOAD_CHANGE = 1
    sdrplay_api_DEVICE_REMOVED = 2
    sdrplay_api_RSP_DUO_MODE_CHANGE = 3
    sdrplay_api_DEVICE_FAIL = 4



# Data Structures
class sdrplay_api_GainCbParamT(Structure):
    _fields_ = [
        ("gRdB", c_uint),
        ("lnaGRdB", c_uint),
        ("currGain", c_double),
    ]

class sdrplay_api_PowerOverloadCbParamT(Structure):
    _fields_ = [
        ("powerOverloadChangeType", sdrplay_api_PowerOverloadCbEventIdT),  # Utilisez c_int pour représenter l'énumération
    ]

class sdrplay_api_RspDuoModeCbParamT(Structure):
    _fields_ = [
        ("modeChangeType", sdrplay_api_RspDuoModeCbEventIdT),  # Utilisez c_int pour représenter l'énumération
    ]

class sdrplay_api_EventParamsT(Union):
    _fields_ = [
        ("gainParams", sdrplay_api_GainCbParamT),
        ("powerOverloadParams", sdrplay_api_PowerOverloadCbParamT),
        ("rspDuoModeParams", sdrplay_api_RspDuoModeCbParamT),
    ]

class sdrplay_api_StreamCbParamsT(Structure):
    _fields_ = [
        ("firstSampleNum", c_uint),
        ("grChanged", c_int),
        ("rfChanged", c_int),
        ("fsChanged", c_int),
        ("numSamples", c_uint),
    ]

sdrplay_api_StreamCallback_t = CFUNCTYPE(
    None,  # Type de retour void
    POINTER(c_short),  # short *xi
    POINTER(c_short),  # short *xq
    POINTER(sdrplay_api_StreamCbParamsT),  # sdrplay_api_StreamCbParamsT *params
    c_uint,  # unsigned int numSamples
    c_uint,  # unsigned int reset
    c_void_p  # void *cbContext
)

sdrplay_api_EventCallback_t = CFUNCTYPE(
    None,  # Type de retour void
    sdrplay_api_EventT,  # sdrplay_api_EventT eventId (utilisez c_int pour représenter l'énumération)
    sdrplay_api_TunerSelectT,  # sdrplay_api_TunerSelectT tuner (utilisez c_int pour représenter l'énumération)
    POINTER(sdrplay_api_EventParamsT),  # sdrplay_api_EventParamsT *params
    c_void_p  # void *cbContext
)

class sdrplay_api_CallbackFnst(Structure):
    _fields_ = [
        ("StreamACbFn", sdrplay_api_StreamCallback_t),  # Pointeur vers une fonction de rappel
        ("StreamBCbFn", sdrplay_api_StreamCallback_t),  # Pointeur vers une fonction de rappel
        ("EventCbFn", sdrplay_api_EventCallback_t),    # Pointeur vers une fonction de rappel
    ]

