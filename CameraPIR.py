import time
import datetime
import picamera
import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.IN)
#with picamera.PiCamera() as camera:
camera = picamera.PiCamera()
i=0
while (1):
        state = GPIO.input(17)
        while(state):
            img_name = "Photo"
            img_name +=str(datetime.datetime.now())
            img_name +=".jpg"
            print (img_name)
            camera.resolution = (2592,1944)
            camera.capture(img_name)
            i=i+1
            time.sleep(1)
            print("takephoto=",i)
            state = GPIO.input(17)
        
