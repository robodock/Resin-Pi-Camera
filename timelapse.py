#!/usr/bin/python

import os, datetime, shutil
import picamera

#time_interval = os.environ["INTERVAL"]

dataDir="/data"
pictureDir=(dataDir + "/capture")

os.chdir(dataDir)

def find_oldest_dir(path) :
	cur_path=os.getcwd()
	os.chdir(path)
	oldestDir = min(os.listdir(path), key=os.path.getctime)
	os.chdir(cur_path)
	return oldestDir

def diskusage(path) :
	st = os.statvfs(path)
	free = st.f_bavail * st.f_frsize
	#total = st.f_blocks * st.f_frsize
	#used = (st.f_blocks - st.f_bfree) * st.f_frsize
	return free 

	
if not os.path.exists(pictureDir) :
	os.makedirs(pictureDir)

# set disk splace limit to 500MB
min=500000

while True :
# check disk space used already
	while diskusage(pictureDir) <= min :
		shutil.rmtree(find_oldest_dir(pictureDir))

	currentHour=datetime.datetime.now().strftime("%Y%m%d_%H")
	if not os.path.exists(os.path.join(pictureDir, currentHour)) :
		os.makedirs(os.path.join(pictureDir, currentHour))
		
	with picamera.PiCamera() as camera:
		camera.resolution=(os.environ["IMAGE_WIDTH"], os.environ["IMAGE_HEIGH"])
		camera.rotation=(270)
	#camera.start_preview()
	#time.sleep(2)
		camera.capture(os.path.join(dataDir,pictureDir,currentHour)+'\/'+datetime.datetime.now().strftime("%Y%M%d-%H%M%S")+'.jpg')
	
	#	for filename in camera.capture_continuous('/data/img-{timestamp:%Y%m%d-%H%M%S}.png'):
	#	print('Captured %s' % filename)
		time.sleep(float(os.environ["TIME_INTERVAL"])) # wait time_interval seconds