#!/usr/bin/env python

from apscheduler.scheduler import Scheduler

def get(refresh=False):
    '''
        A python singleton to create and start a scheduler
        the first time it's called and return the instance
        on subsequent calls.
    '''
    if refresh:
        get.sched = None
    if get.sched:
        return get.sched
    # create a scheduler
    get.sched = Scheduler(coalesce=True)
    # start it
    get.sched.start()
    return get.sched

get.sched = None


