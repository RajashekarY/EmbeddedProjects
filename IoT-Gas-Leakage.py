from time import sleep
import RPi.GPIO as GPIO       ## Import GPIO library
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)## Use board pin numbering
import os
import urllib2
import urllib
gas=29
buz=31
HIGH=1
LOW=0
GPIO.setup(gas, GPIO.IN)            # initialize GPIO Pin as inputs
GPIO.setup(buz, GPIO.OUT)            # initialize GPIO Pin as output
input_state = GPIO.input(gas)
def buzzer(times):
    for i in range(times):
        GPIO.output(buz, HIGH)
        sleep(1)
        GPIO.output(buz, LOW)
        sleep(2)
while True:
##    if input_state == False:
##        print'Gas Leaking'
##    elif input_state == True:
##        print "all is well"

    if GPIO.input(gas)==0:
        buzzer(25)
        gas_message="Gas is leaking at location"
        server="https://api.thingspeak.com/update?api_key=G4VUD4ELENIZRY31&field1="
        g=str(gas)
        url=server+g
        f = urllib.urlopen(url)
        sleep(5)
        message=server+gas_message
        ff = urllib.urlopen(message)
        print "Upload done Successfully"
    
 
