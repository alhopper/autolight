#!/usr/bin/env python

import datetime
import ephem 

o = ephem.Observer()
o.lat, o.long, o.date = '33:2:7', '-96:44:8', ephem.now()
o.elevation = 600
sun = ephem.Sun(o)
print "Plano, TX "
print "sunrise:", ephem.localtime(o.next_rising(sun))
print "sunset:", ephem.localtime(o.next_setting(sun))





