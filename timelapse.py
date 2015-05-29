#!/usr/bin/python

import time
import picamera

with picamera.PiCamera() as camera:
#    camera.start_preview()
#    time.sleep(2)
    for filename in camera.capture_continuous('/data/img-{timestamp:%Y%m%d-%H%M%S}.png'):
        print('Captured %s' % filename)
        time.sleep(10) # wait 10 seconds