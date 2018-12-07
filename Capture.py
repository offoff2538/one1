import RPi.GPIO as GPIO
import time
import os
import picamera
count =0
step=0
input_pin1=18
input_pin2=27
input_pin3=22
buzzer_pin=7
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(input_pin1,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(input_pin2,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(input_pin3,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(buzzer_pin,GPIO.OUT)
buzzer=GPIO.PWM(buzzer_pin,1000)
def sound():
    buzzer.start(50)
    time.sleep(0.3)
    buzzer.start(0)
while(1):
    state1=GPIO.input(input_pin1)
    state2=GPIO.input(input_pin2)
    state3=GPIO.input(input_pin3)
    if(state1==GPIO.LOW):
        sound()
        count=count+1
        os.system("raspivid -t 3000 -o vid"+str(count)+".h264")
        print("count=",count)
    if(state2==GPIO.LOW):
        sound()
        os.system("omxplayer vid"+str(step)+".h264")
        step=step+1
        print("step=",step)
    if(state3==GPIO.LOW):
        sound()
        if(step!=0):
            step=step-1 
        os.system("omxplayer vid"+str(step)+".h264")
        print("step=",step)
               

