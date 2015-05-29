#!/usr/bin/python

import time
import picamera

with picamera.PiCamera() as camera:
#    camera.start_preview()
#    time.sleep(2)
    camera.capture_continuous('/data/{timestamp:%Y}/{timestamp:%m}/{timestamp:%d}/img-{timestamp:%H%M%S}.png')
#        print('Captured %s' % filename)
    time.sleep(10) # wait 10 seconds