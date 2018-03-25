#!/usr/bin/env python3

import time
import RPi.GPIO as GPIO

GRELAY = 22


def init_gpio():
    GPIO.setwarnings(False)
    # setup GPIO, use board connector pin numbering.
    GPIO.setmode(GPIO.BCM)
    # setup GRELAY pin as an output
    GPIO.setup(GRELAY, GPIO.OUT)
    # Turn off the relay
    turn_off_light()


def turn_on_light():
    GPIO.output(GRELAY, GPIO.HIGH)


def turn_off_light():
    GPIO.output(GRELAY, GPIO.LOW)


def cycle_light():
    turn_on_light()
    time.sleep(2.6)
    turn_off_light()


def init_rpi_io():
    init_gpio()

