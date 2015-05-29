#!/usr/bin/python

import picamera

with picamera.PiCamera() as camera:
    camera.resolution = (640, 480)
    camera.start_recording('/data/my_video.h264')
    camera.wait_recording(60)
    camera.stop_recording()