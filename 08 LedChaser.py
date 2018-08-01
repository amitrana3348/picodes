import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(7,GPIO.OUT)
GPIO.setup(8,GPIO.OUT)
GPIO.setup(12,GPIO.OUT)
GPIO.setup(16,GPIO.OUT)
GPIO.setup(20,GPIO.OUT)
GPIO.setup(21,GPIO.OUT)
GPIO.setup(24,GPIO.OUT)
GPIO.setup(25,GPIO.OUT)
while True:
    GPIO.output(8,GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(8,GPIO.LOW)
    
    
    GPIO.output(7,GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(7,GPIO.LOW)
  

    GPIO.output(12,GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(12,GPIO.LOW)
    
    GPIO.output(16,GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(16,GPIO.LOW)
    
    GPIO.output(20,GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(20,GPIO.LOW)
    
    GPIO.output(21,GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(21,GPIO.LOW)
    
    GPIO.output(24,GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(24,GPIO.LOW)
    
    GPIO.output(25,GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(25,GPIO.LOW)
   
