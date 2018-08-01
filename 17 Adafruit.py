from Adafruit_IO import*
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(27,GPIO.OUT)
while True:
    aio=Client('your_key')
    aio.send('temp',35)
    data=aio.receive('led')
    print data
    print data.value
    if(data.value == 'ON'):
        print 'on'
        GPIO.output(27,GPIO.HIGH)
    else:
        print 'else'
        GPIO.output(27,GPIO.LOW)
