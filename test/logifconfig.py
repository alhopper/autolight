#!/usr/bin/python

import string
import subprocess


def get_inet_addr():
    p = subprocess.Popen(['/sbin/ifconfig', '-a'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out,err = p.communicate()
    firstpass = True
    start = 0
    results = []
    while firstpass or found:
        firstpass = False
        start = string.find(out,'inet addr', start)
        found = (start >= 0)
        if found:
            end = string.find(out,'\n',start)
            results.append(out[start:end])
            start = end
    return results

results = get_inet_addr()
for r in results:
    print 'result:', r
