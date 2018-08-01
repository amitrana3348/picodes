import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
sw=26
GPIO.setup(sw,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
count=0
while True:
    if(GPIO.input(sw)==1):
        count=count+1;
        print("count is",str(count))
        time.sleep(1)
