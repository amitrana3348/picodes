#Program to blink all LED's


import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)          #To use GPIO numbering system
GPIO.setup(24,GPIO.OUT)         #Set pin no 24 as an output pin
GPIO.setup(25,GPIO.OUT)
GPIO.setup(8,GPIO.OUT)
GPIO.setup(7,GPIO.OUT)
GPIO.setup(12,GPIO.OUT)
GPIO.setup(16,GPIO.OUT)
GPIO.setup(20,GPIO.OUT)
GPIO.setup(21,GPIO.OUT)
while True:
    GPIO.output(24,GPIO.HIGH)   #Set pin no 24 to HIGH 
    GPIO.output(25,GPIO.HIGH)
    GPIO.output(8,GPIO.HIGH)
    GPIO.output(7,GPIO.HIGH)
    GPIO.output(12,GPIO.HIGH)
    GPIO.output(16,GPIO.HIGH)
    GPIO.output(20,GPIO.HIGH)
    GPIO.output(21,GPIO.HIGH)
    time.sleep(1)               #Delay of 1sec
    GPIO.output(24,GPIO.LOW)    #Set pin no 24 to LOW
    GPIO.output(25,GPIO.LOW)
    GPIO.output(8,GPIO.LOW)
    GPIO.output(7,GPIO.LOW)
    GPIO.output(12,GPIO.LOW)
    GPIO.output(16,GPIO.LOW)
    GPIO.output(20,GPIO.LOW)
    GPIO.output(21,GPIO.LOW)
    time.sleep(1)
