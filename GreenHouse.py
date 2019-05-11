from time import sleep
import RPi.GPIO as GPIO       ## Import GPIO library
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)      ## Use board pin numbering
import urllib2
import cookielib
from getpass import getpass
import sys
import os
from stat import *
from urllib import urlencode
import urllib
soil=32
humi=36
temp=37
ldr=38
fan=29
motor=31
HIGH=1
LOW=0
GPIO.setup(soil, GPIO.IN)            # initialize GPIO Pin as outputs
GPIO.setup(humi, GPIO.IN)            # initialize GPIO Pin as input
GPIO.setup(temp, GPIO.IN)            # initialize GPIO Pin as outputs
GPIO.setup(ldr, GPIO.IN)            # initialize GPIO Pin as input

#GPIO.setup(buzz, GPIO.OUT)      ## Setup GPIO Pin 11 to OUT
GPIO.setup(fan, GPIO.OUT)
GPIO.setup(motor, GPIO.OUT)
#GPIO.setup(m2b, GPIO.OUT)
def buzzer(times):
    for i in range(0,times):
        GPIO.output(buzz, HIGH)
    #GPIO.output(led, LOW)
        #time.sleep(0.01)
        sleep(0.5)
        GPIO.output(buzz, LOW)
#buzzer(10)
Light='https://api.thingspeak.com/update?api_key=KFM41ABKMCOSM5PF&field1='
Humidity='https://api.thingspeak.com/update?api_key=KFM41ABKMCOSM5PF&field2='
Temp='https://api.thingspeak.com/update?api_key=KFM41ABKMCOSM5PF&field3='
Smoisture='https://api.thingspeak.com/update?api_key=KFM41ABKMCOSM5PF&field4='
while True:
    if GPIO.input(ldr)==1:
        GPIO.output(fan, HIGH)                                
        #sms("Gas leaking in your Factory")
        l=str(ldr)
        url1=Light+l
        f = urllib.urlopen(url1)
        print("Light Present")
        #buzzer(25)
    elif GPIO.input(humi)==1:#water==0:
        h=str(humi)
        GPIO.output(fan, HIGH)
        
        #sms("water leaking in your Factory")
        print("water leaking in your Factory")
        url2=Humidity+h
        f = urllib.urlopen(url2)
        #buzzer(25)
    elif GPIO.input(temp)==1:#temp==0:
        GPIO.output(motor, HIGH)
        #sms("High Temprarure Detected In Factory")
        print("High Temprarure Detected In Factory")
        GPIO.output(motor, HIGH)
        #buzzer(25)
        t=str(temp)
        url3=Temp+t
        f = urllib.urlopen(url3)
    elif GPIO.input(soil)==1:#temp==0:
        print("Soil Moisture Available")
        #buzzer(25)
        s=str(soil)
        url4=Smoisture+s
        f = urllib.urlopen(url4)
    
