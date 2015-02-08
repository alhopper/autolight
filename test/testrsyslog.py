#!/usr/bin/python


import logging
import logging.handlers
from syslog import syslog

log = logging.getLogger('testfromRPi')
log.setLevel(logging.DEBUG)
handler = logging.handlers.SysLogHandler(address='/dev/log')
handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
log.addHandler(handler)
print 'info level enabled?', log.isEnabledFor(logging.INFO)

log.info("info level log msg")
log.debug("test: debug level log msg")
