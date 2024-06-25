from picamera2 import PiCamera2
from time import sleep

camera = PiCamera2()

camera.start_preview()
sleep(5)
camera.stop_preview()