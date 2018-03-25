#!/usr/bin/env python3


from bibliopixel.drivers.serial import  *
from bibliopixel import LEDStrip

#init driver with the type and count of LEDs you're using
driver = Serial(ledtype=LEDTYPE.WS2812B, num=146)

#init controller
led = LEDStrip(driver)

led.all_off()
led.update()
