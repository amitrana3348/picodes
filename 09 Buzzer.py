import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(8,GPIO.OUT)
while True:
    GPIO.output(18,GPIO.HIGH)
    GPIO.output(8,GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(18,GPIO.LOW)
    GPIO.output(8,GPIO.LOW)
    time.sleep(1)
    
    
