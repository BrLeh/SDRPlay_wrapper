# SDRPlay_wrapper

WIP Python wrapper to handle SDRPlay C++ API.

Only works on Linux and tested on Ubuntu 22.04. At the moment, I only tested this library with SDRPlay rspdx-r2 SDR.

# Installation

You need numpy version >= 2.2.6.

After cloning the repo, go to the repo location and run :

```
$ pip install -e .
```

# Quick start

Connect one SDRPlay SDR model to the computer USB port.

Run tests/test.py

## Expected output
```
1 SDRplay detected:
- Device 0: Serial Number XXXXXXXX,7,None
SDRplay succesfully connected: XXXXXXXX,7,1,1,35605248,
[SDR] Initializing...
[Thread] IQ consumer thread started
[SDR] Record started
[Callback] IQ samples received, numSamples=1008
```

# TO DO

- Handle Windows OS
- Incluse missing SDRPlay API functions in the wrapper

  
