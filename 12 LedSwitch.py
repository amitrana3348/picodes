import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(26,GPIO.IN)
GPIO.setup(19,GPIO.IN)
GPIO.setup(13,GPIO.IN)
GPIO.setup(6,GPIO.IN)

GPIO.setup(24,GPIO.OUT)
GPIO.setup(25,GPIO.OUT)
GPIO.setup(8,GPIO.OUT)
GPIO.setup(7,GPIO.OUT)
GPIO.setup(12,GPIO.OUT)
GPIO.setup(16,GPIO.OUT)
GPIO.setup(20,GPIO.OUT)
GPIO.setup(21,GPIO.OUT)

GPIO.setup(26,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(19,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(13,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(6,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
while True:
    if(GPIO.input(26)== 0):
        GPIO.output(24,GPIO.HIGH)
        GPIO.output(25,GPIO.HIGH)
        
    if(GPIO.input(26)== 1):
        GPIO.output(24,GPIO.LOW)
        GPIO.output(25,GPIO.LOW)
        
        
    if(GPIO.input(19)== 0):
        GPIO.output(8,GPIO.HIGH)
        GPIO.output(7,GPIO.HIGH)
        
    if(GPIO.input(19)== 1):
        GPIO.output(8,GPIO.LOW)
        GPIO.output(7,GPIO.LOW)
        
        
    if(GPIO.input(13)==0):
        GPIO.output(12,GPIO.HIGH)
        GPIO.output(16,GPIO.HIGH)
        
    if(GPIO.input(13)== 1):
        GPIO.output(12,GPIO.LOW)
        GPIO.output(16,GPIO.LOW)
        
        
    if(GPIO.input(6)== 0):
        GPIO.output(20,GPIO.HIGH)
        GPIO.output(21,GPIO.HIGH)
       
    if(GPIO.input(6)== 1):
        GPIO.output(20,GPIO.LOW)
        GPIO.output(21,GPIO.LOW)
        
        
 
