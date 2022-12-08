#!/usr/bin/env python3


from bibliopixel.drivers.serial import  *
from bibliopixel import LEDStrip

#init driver with the type and count of LEDs you're using
driver = Serial(num=76, ledtype=LEDTYPE.LPD8806)

#init controller
led = LEDStrip(driver)

led.all_off()
led.update()
