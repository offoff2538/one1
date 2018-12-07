import time
import picamera
import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(18,GPIO.IN,pull_up_down=GPIO.PUD_UP)
with picamera.PiCamera() as camera:
	camera.resolution = (1024,768)
	camera.start_preview()
	GPIO.wait_for_edge(18, GPIO.FALLING)
	camera.capture('SW_C1.jpg')

