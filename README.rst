=========
AutoLight
=========

Introduction
------------

Like a lot of projects, this one was done to scratch an itch.
I was frustrated by several security lights that have
an automatic, light sensitive, control system that never seems to
be able to tell the difference between day and night!

Since day and night are governed by the position of the Sun, it
became clear that the only way to resolve my frustration was to 
calculate accurate times for Sunrise and Sunset and control the
security light on/off times with this knowledge.

Enter the Raspberry Pi (RPi) microcontroller and a couple of 
high-quality accessories parts and some Python code.  Problem 
solved!  :)

Yes I know that there are commercial sunrise/sunset switches 
available - but it's much more fun to build it yourself.

Design Goals
------------

The RPi Sunrise/Sunset should meet the following goals; it should:

* have a minimum number of mechanical parts for reliability.  

  * *solution:* use a Solid State Relay (SSR)

* be able to keep time without an ethernet connection.

  * *solution:* install a battery backed Real Time clock

* keep time, even after power interruption.  

  * *solution:* install a battery backed Real Time clock

* given an ethernet connection, preferably WiFi, it should log its actions - preferably via an on-line logging service.

  * *solution:* use **PaperTrail** (see below)

* given an ethernet connection, it should provide a visual *heartbeat*, preferably via an online service, so that it's *health* status can be quickly verified.

  * *solution:* use **Librato** (see below)

* be low-cost

* be reasonably safe - from an electrical standpoint.

  * *solution:* install a fuse in the A/C circuit.

* have a reasonably small code-base that is easy to maintain and extend for other applications.

  * *solution:* *Python* and it's high quality contributed software code-base **rocks**. [#]_


*"Build on the work or others"*
-----------------------------

This project would not be possible without the following *awesome* Python modules:

* **PyEphem** `provides an ephem Python package for performing high-precision astronomy computations <https://pypi.python.org/pypi/pyephem//>`_
* **APScheduler** `Advanced Python Scheduler <https://pypi.python.org/pypi/APScheduler/2.1.1/>`_

Recommended Parts List
----------------------

* RPi model A, if the ethernet hardware is not required. Otherwise use the Model B
* RPi compaible WiFi USB dongle

  * use anything RPi compatible that is *on-sale*!

* Solid State Relay (SSR) board 

  * for (up to a) 2 Amp load: use the **SainSmart** `2 channel 2A SSR board <http://www.sainsmart.com/arduino-compatibles-1/relay/solid-state-relay/sainsmart-2-channel-5v-solid-state-relay-module-board-omron-ssr-avr-dsp-arduino.html>`_
  * for (up to a) 5 Amp load: use the **SainSmart** `2 channel 5A SSR board <http://www.sainsmart.com/arduino-compatibles-1/relay/solid-state-relay/sainsmart-2-channel-ssr-2f-solid-state-relay-3v-32v-5a-for-avr-dsp-arduino-mega-uno-r3.html/>`_

* RPi battery backed RTC module

  * **RasClock** `Raspberry Pi Real Time Clock Module <http://afterthoughtsoftware.com/products/rasclock>`_
  * Available from `Acme Unlimited <http://store.acmeun.com/products/rasclock-raspberry-pi-real-time-clock-module.html>`_

* Appropriate fuse and fuse holder (Radio Shack or your local hardware store)
* Appropriate (plastic) box

Validation and Testing
----------------------

The codebase is small and simple and while there is never an excuse for a lack of automated 
testing, the only test that seems necessary, is one to establish the basic accuracy of the
Sunrise/Sunset calculations.  To validate the calculations, you'll find an *"eyeball"* (sorry)
test in the test subdirectory.  Execute the following standalones and *eyeball* the results:
::

  test/sunrisesunset-ephem.py
  test/sunrisesunset-usno.py


Recommended On-line Services
----------------------------
Both these sevice providers are **awesome**.  You may be able to stay within the *free* usage limits if you're just using them for this project.  But you will quickly start using them for many other projects!!  ;-)

**PaperTrail** `On-line Logging Service <https://papertrailapp.com/>`_

Here is a sample logging output |LOG|

.. |LOG| image:: autolight/doc/images/autolight-papertrail-grab.png

**Librato** `On-line real-time dashboard/plotting service <https://metrics.librato.com/>`_

Here is a sample of the activity output plot |PLOT|

.. |PLOT| image:: autolight/doc/images/autolight-librato-grab.png

------------

.. [#] Python is a *first-class* supported development environment within the RPi eco-system.
