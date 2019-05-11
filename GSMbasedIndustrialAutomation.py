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
water=32
gas=36
temp=37
buzz=38
fan=29
motor=31
HIGH=1
LOW=0
GPIO.setup(water, GPIO.IN)            # initialize GPIO Pin as outputs
GPIO.setup(gas, GPIO.IN)            # initialize GPIO Pin as input
GPIO.setup(temp, GPIO.IN)            # initialize GPIO Pin as outputs
#GPIO.setup(, GPIO.IN)            # initialize GPIO Pin as input

GPIO.setup(buzz, GPIO.OUT)      ## Setup GPIO Pin 11 to OUT
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
def sms(message):
    #message = """raw_input("Enter text: ")"""

    number = "8686563675"
    message = urlencode({'message':message})
    message = message[message.find("=")+1:]
    if __name__ == "__main__":    
        username = "8686563675"
        passwd = "T9282C"

        message = "+".join(message.split(' '))

     #logging into the sms site
        url ='http://site24.way2sms.com/Login1.action?'
        data = 'username='+username+'&password='+passwd+'&Submit=Sign+in'

     #For cookies

        cj= cookielib.CookieJar()
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))

     #Adding header details
        opener.addheaders=[('User-Agent','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.120')]
        try:
            usock =opener.open(url, data)
        except IOError:
            print "error"
            #return()

        jession_id =str(cj).split('~')[1].split(' ')[0]
        send_sms_url = 'http://site24.way2sms.com/smstoss.action?'
        send_sms_data = 'ssaction=ss&Token='+jession_id+'&mobile='+number+'&message='+message+'&msgLen=136'
        opener.addheaders=[('Referer', 'http://site25.way2sms.com/sendSMS?Token='+jession_id)]
        try:
            sms_sent_page = opener.open(send_sms_url,send_sms_data)
        except IOError:
            print "error"
            #return()

        print "success" 
while True:
    if GPIO.input(gas)==1:
        GPIO.output(fan, HIGH)                                
        sms("Gas leaking in your Factory")
        print("Gas leaking in your Factory")
        buzzer(25)
    elif GPIO.input(water)==0:#water==0:
        sms("water leaking in your Factory")
        print("water leaking in your Factory")
        buzzer(25)
    elif GPIO.input(temp)==1:#temp==0:
        GPIO.output(motor, HIGH)
        sms("High Temprarure Detected In Factory")
        print("High Temprarure Detected In Factory")
        buzzer(25)
    elif GPIO.input(gas)==1 or GPIO.input(water)==1 or GPIO.input(temp)==1:
        sms("Abnormality found in factory check")
        print("Abnormality found in factory check")
    else:
        print"all is well"
    
