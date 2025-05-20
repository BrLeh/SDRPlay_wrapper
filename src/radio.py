from _wrapper import sdrplay_api,sdrplay_api_DeviceT,sdrplay_api_DeviceParamsT,sdrplay_api_RxChannelParamsT,sdrplay_api_Bw_MHzT,sdrplay_api_If_kHzT,sdrplay_api_AgcControlT,sdrplay_api_RspDx_AntennaSelectT,sdrplay_api_CallbackFnst
from _wrapper import SDRStreamHandler
import ctypes

MAX_DEVICES = 1 #MAXIMUM NUMBER OF DEVICE


class MyRadio:
    def __init__(self):
        handle = ctypes.c_void_p()
        err=sdrplay_api.sdrplay_api_Open()
        if err!=0:
            raise RuntimeError("Failed to initialize radio")

        sdrplay_api.sdrplay_api_LockDeviceApi()

    def get_devices(self,verbose=True):
        devices = (sdrplay_api_DeviceT * MAX_DEVICES)()
        self.p_devices=ctypes.POINTER(sdrplay_api_DeviceT)(devices)
        self.num_devices = ctypes.POINTER(ctypes.c_int)(ctypes.c_int(0))

        err = sdrplay_api.sdrplay_api_GetDevices(self.p_devices, self.num_devices, MAX_DEVICES)
        if err == 0 and self.num_devices.contents.value > 0 and verbose==True:
            print(f"{self.num_devices.contents.value} SDRplay detected:")
            for i in range(self.num_devices.contents.value):
                print(f"- Device {i}: Serial Number {self.p_devices[i].SerNo.decode()},{self.p_devices[i].hwVer},{self.p_devices[i].dev}")
        else:
            raise RuntimeError("No device detected")

    def connect(self,verbose=True):
        self.p_device=ctypes.POINTER(sdrplay_api_DeviceT)(self.p_devices[0])
        err = sdrplay_api.sdrplay_api_SelectDevice(self.p_device)

        if err == 0 and verbose==True:
            print(f"SDRplay succesfully connected: {self.p_device.contents.SerNo.decode()},{self.p_device.contents.hwVer},{self.p_device.contents.tuner.value},{self.p_device.contents.valid},{self.p_device.contents.dev},")
        else:
            raise RuntimeError("Error when trying to connect to the device")
        
        sdrplay_api.sdrplay_api_UnlockDeviceApi()


        device_params = sdrplay_api_DeviceParamsT()
        sdrplay_api.sdrplay_api_GetDeviceParams.argtypes=[ctypes.c_void_p,ctypes.POINTER(ctypes.POINTER(sdrplay_api_DeviceParamsT))]
        self.p_device_params=ctypes.pointer(device_params)
        err = sdrplay_api.sdrplay_api_GetDeviceParams(ctypes.c_void_p(self.p_device.contents.dev),ctypes.pointer(self.p_device_params))

        if err != 0:
            sdrplay_api.sdrplay_api_Close()
            raise RuntimeError("Cannot get device parameters")
        
        self.chParams = sdrplay_api_RxChannelParamsT()
        self.chParams = self.p_device_params.contents.rxChannelA
    
    def start(self):
        cbFns=sdrplay_api_CallbackFnst()
        handler=SDRStreamHandler(sdrplay_api,self.p_device,cbFns)
        handler.start()
        
    def set_frequency(self,frequencyHz:float):
        self.chParams.contents.tunerParams.rfFreq.rfHz=frequencyHz
    def set_bandwidth(self,bandwidth:sdrplay_api_Bw_MHzT):
        self.chParams.contents.tunerParams.bwType  = bandwidth
    def set_ifType(self,ifType:sdrplay_api_If_kHzT):
        self.chParams.contents.tunerParams.ifType = ifType  
    def set_gaindB(self,gaindB:int):
        self.chParams.contents.tunerParams.gain.gRdB = gaindB
    def set_LNAstate(self,state:int):
        self.chParams.contents.tunerParams.gain.LNAstate = ctypes.c_uint(state)
    def set_agcStatus(self,agcStatus:sdrplay_api_AgcControlT):
        self.chParams.contents.ctrlParams.agc.enable = agcStatus
    def set_agcSensitivity(self,sensitivity:float):
        self.chParams.contents.ctrlParams.agc.setPoint_dBfs = sensitivity
    def select_antenna(self,antenna:sdrplay_api_RspDx_AntennaSelectT):
        self.p_device_params.contents.devParams.contents.rspDxParams.antennaSel= antenna
    def set_biasT(self,status:int):
        self.p_device_params.contents.devParams.contents.rspDxParams.biasTEnable= ctypes.c_ubyte(status)



if __name__=='__main__':
    a=MyRadio()
    a.get_devices()
    a.connect()
    a.start()
    
    

    
    
        

