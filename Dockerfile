FROM resin/rpi-raspbian:jessie

# Install Python, pip and the camera module firmware
RUN apt-get update && apt-get install -y python python-dev libraspberrypi-bin python-pip dropbear openssh-client

# Install picamera python module using pip
RUN pip install picamera
RUN cp /usr/share/zoneinfo/Asia/Taipei /etc/localtime


# add the root dir to the /app dir in the container env
COPY . /app

CMD modprobe bcm2835-v4l2 && /app/start.sh
#CMD ["bash", "/app/start.sh"]
