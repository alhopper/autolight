#!/usr/bin/env python3

from bibliopixel.drivers.serial import  *
from bibliopixel import LEDStrip
import bibliopixel.colors as colors
from BiblioPixelAnimations.strip import ColorFill

#init driver with the type and count of LEDs you're using
driver = Serial(ledtype=LEDTYPE.WS2812B, num=146)

#init controller
led = LEDStrip(driver)

#init animation; replace with whichever animation you'd like to use
# actually G, R, B
# good orange acolor = (57, 230, 0)
acolor = (57, 240, 0)
# col = colors.color_scale(acolor, 140)
# 1.5A at 200, best visual at 140 -> 180
col = colors.color_scale(acolor, 180)
anim = ColorFill.ColorFill(led, col)

#run the animation
anim.run()
