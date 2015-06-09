#!/usr/bin/python

import os
import time
import picamera

time_interval = os.environ["INTERVAL"]

with picamera.PiCamera() as camera:
#    camera.start_preview()
#    time.sleep(2)
    for filename in camera.capture_continuous('/data/img-{timestamp:%Y%m%d-%H%M%S}.png'):
#        print('Captured %s' % filename)
        time.sleep(float(time_interval)) # wait time_interval seconds