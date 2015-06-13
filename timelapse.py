#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 16:21:33 2015
Raspberry Pi timelapse camera for Resin.io
picture save into hourly folder in /data/capture,
remove oldest hour when disk full.
get picture resolution from Environment variables IMAGE_WIDTH, IMAGE_HEIGHT
get timelaspe interval from Environment variables TIME_INTERVAL
@author: eddie@robodock.net
"""

import os, time, datetime, shutil
import picamera


dataDir="/data"
pictureDir=dataDir + "/capture"


def find_oldest_dir(path) :
	os.chdir(path)
	oldestDir = min(os.listdir(path), key=os.path.getctime)
	return oldestDir

def diskusage(path) :
	st = os.statvfs(path)
	free = st.f_bavail * st.f_frsize
	#total = st.f_blocks * st.f_frsize
	#used = (st.f_blocks - st.f_bfree) * st.f_frsize
	return free 


os.chdir(dataDir)
	
if not os.path.exists(pictureDir) :
	os.makedirs(pictureDir)

# set disk free space safe limit to 500MB
min=500000000

while True :

	while diskusage(pictureDir) <= min :
		shutil.rmtree(find_oldest_dir(pictureDir))

	currentHour=datetime.datetime.now().strftime("%Y%m%d_%H")
	if not os.path.exists(os.path.join(pictureDir, currentHour)) :
		os.makedirs(os.path.join(pictureDir, currentHour))
		
	with picamera.PiCamera() as camera:
		camera.resolution=(int(os.environ["IMAGE_WIDTH"]), int(os.environ["IMAGE_HEIGH"]))
		camera.rotation=(270) #my camera angle
		camera.capture(os.path.join(pictureDir,currentHour)+'/'+datetime.datetime.now().strftime("%Y%m%d-%H%M%S")+'.png')
		time.sleep(float(os.environ["TIME_INTERVAL"])) # wait time_interval seconds