#!/usr/bin/env python

import urllib
import httplib
import string
import re
from BeautifulSoup import BeautifulSoup
from datetime import datetime


def stripit(ipstr):
    return string.strip(ipstr)


def cleanupResults(results):
    '''
        Extract and cleanup the returned HTML.
        Retrn a pipe seperated list.
    '''
    pipeSeparatedData = []
    status = results.status
    if status == 200:
        data = results.read()
        soup = BeautifulSoup(data)
        target_HTML = soup.first('pre') # grab text inside <pre html tags
        # break it up into lines
        targetLines = []
        for line in target_HTML:
            targetLines.append(line)
        # we're interested in line 2
        # break it down to a list
        sunriseDataList = targetLines[2].split('\n')
        # strip leading/trailing space
        sunriseDataList = map(stripit, sunriseDataList)
        # remove empty members
        sunriseDataList = filter(None, sunriseDataList)
        # parse line to produce pipe separated name/value string
        for en in sunriseDataList:
            icu = re.sub(r'  +', '|', en)
            pipeSeparatedData.append(icu)
        # sample output
        # [u'Begin civil twilight|6:56 a.m.', u'Sunrise|7:21 a.m.', u'Sun transit|1:32 p.m.',
        # u'Sunset|7:44 p.m.', u'End civil twilight|8:08 p.m.']
    else:
        print 'Error from Sunrise/Sunset website - no data available'
    return pipeSeparatedData


def findRequestedTime(description, datalist):
    '''
        Return the data associated with a tag in a pipe separated input string.
    '''
    for data in datalist:
        if data.lower().find(description) >= 0:
            return data.split('|')[1]
    return None


def sampleQueries(data):
    '''
        Print the sunrise/sunset data in chronological order.
    '''
    print 'Todays Sunrise and Sunset times in chronological order:'
    print 'begin civil twilight %s' % findRequestedTime('begin civil twilight', data)
    print 'sunrise %s' % findRequestedTime('sunrise', data)
    print 'transit %s' % findRequestedTime('transit', data)
    print 'sunset %s' % findRequestedTime('sunset', data)
    print 'end civil twilight %s' % findRequestedTime('end civil twilight', data)


def main():
    '''
        mainline: connect to the US Navy Observatory and "pretend" to fill in a
        request form to get the Sunrise/Sunset data for today.
    '''
    conn = httplib.HTTPConnection('aa.usno.navy.mil', 80)
    today = datetime.today()
    year = today.strftime('%Y')
    month = today.strftime('%m')
    day = today.strftime('%d')
    params = urllib.urlencode({'FFX':1, 'ID':'LOG', 'xxy':year, 'xxm':month, 'xxd':day, 'st':'TX', 'place':'plano', 'ZZZ':'END'})
    headers = {'Content-type': 'application/x-www-form-urlencoded', 'Accept': 'text/html'}
    conn.request('POST', '/cgi-bin/aa_pap.pl', params, headers)
    resp = conn.getresponse()
    pipeSeparatedData = cleanupResults(resp)
    conn.close()
    return pipeSeparatedData

if __name__ == "__main__":
    usno_data = main()
    sampleQueries(usno_data)
