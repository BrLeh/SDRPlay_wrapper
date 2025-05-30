from SDRPlay_wrappy.radio import MyRadio


a=MyRadio()
a.get_devices()
a.connect()
a.start()