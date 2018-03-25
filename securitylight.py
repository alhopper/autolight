#!/usr/bin/env python3

import time
from autolight.Automaticlight import main

if __name__ == '__main__':
    '''
        An application to turn on/off power to equipment, e.g., security lights,
        at Sunset/Sunrise.  Uses the Raspberry Pi (RPi) computer and a low-cost
        Solid State Relay (board) to switch the A/C to the device(s). 
        See the README for additional details.
    '''
    main()
    # this sleep functions only purpose is to generate enough "work" to provide
    # an "activity plot" (in librato) that's not a flat line.  See the heartbeat() 
    # function in the code.
    while True:
        time.sleep(17)
