import time
import RPi.GPIO as GPIO
GPIO.cleanup()
GPIO.setmode(GPIO.BCM)
GPIO.setup(21,GPIO.OUT)
while True:
    GPIO.setwarnings(False)
    GPIO.output(21,True)
    time.sleep(2)
    GPIO.output(21,False)
    time.sleep(2)
    