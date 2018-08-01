import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(27,GPIO.OUT)
GPIO.setup(8,GPIO.OUT)
while True:
    GPIO.output(27,GPIO.HIGH)
    GPIO.output(8,GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(27,GPIO.LOW)
    GPIO.output(8,GPIO.LOW)
    time.sleep(0.5)
    
    
