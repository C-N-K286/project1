import sys
import Adafruit_DHT
import requests
import mcp3008
import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(21,GPIO.OUT)
GPIO.setwarnings(False)
import ultr as u
url = "http://10.0.3.23:9876/temperature/get/"
while True:
    y = time.ctime();
    humidity,temperature = Adafruit_DHT.read_retry(11,4)
    temperature=int(temperature)
    z = ((1024-mcp3008.readadc(3))/1024.0) * 100;
    #h =float((z/1024)
    x = {'temperature': temperature,'humidity':int(humidity),'time':y,'moisture':z}
    u.ult()
    print x
    #time.sleep(1)
    if(z < 60):
        print 'nsk'
        z = ((1024-mcp3008.readadc(3))/1024.0) * 100;
        GPIO.output(21,GPIO.HIGH)
    else:
        GPIO.output(21,False)