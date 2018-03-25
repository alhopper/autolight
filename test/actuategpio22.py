#!/usr/bin/env python3

from time import *
import RPi.GPIO as GPIO
import logging
import sys

# initialize GPIO hardware to factory default
# GPIO.cleanup()

def init_gpio(relay):
    GPIO.setwarnings(False)
    # setup GPIO, use board connector pin numbering.
    GPIO.setmode(GPIO.BCM)
    # setup relay pin as an output
    GPIO.setup(relay, GPIO.OUT)
    # Turn off relay
    GPIO.output(relay, GPIO.LOW)

def turn_on_light(relay):
    # Turn on relay
    GPIO.output(relay, GPIO.HIGH)

def turn_off_light(relay):
    # Turn off relay
    GPIO.output(relay, GPIO.LOW)

def cycle_light(relay):
    # Turn on 
    turn_on_light(relay)
    sleep(2.6)
    # Turn off 
    turn_off_light(relay)


def main():
    try:
        init_gpio(GRELAY)
    except Exception, err:
        print 'err:', err
        return 1
    else:
        cycle_light(GRELAY)
        return 0

GRELAY = 22
if __name__ == '__main__':
    sys.exit(main())
