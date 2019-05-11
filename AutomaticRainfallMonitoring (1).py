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
buz=29
water=31
motor=33
rain=35
HIGH=1
LOW=0
GPIO.setup(water, GPIO.IN, pull_up_down=GPIO.PUD_UP)            # initialize GPIO Pin as outputs
GPIO.setup(motor, GPIO.OUT)            # initialize GPIO Pin as output
GPIO.setup(rain, GPIO.IN, pull_up_down=GPIO.PUD_UP)            # initialize GPIO Pin as outputs
GPIO.setup(buz, GPIO.OUT)

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
server="https://api.thingspeak.com/update?api_key=X4Q901AXG9I788QJ&field1="
print "Automatic Rainfall Monitoring System Using IoT"
print "Caliberating All...Sensors \n"
for i in range(10):
    print ".",
    sleep(.3)
sleep(5)
print "Caliberation Completed \n It Started Working"
while True:
    if GPIO.input(rain)==1:
        sms("Its Raining")
        if GPIO.input(water)==1:
            sms("Rain Filled The Space")
            k1="It's raining and water level is HIGH!!!"
            print k1
            finally_=server+k1
            f = urllib.urlopen(finally_)

            GPIO.output(motor, GPIO.HIGH)
        elif GPIO.input(water)==0:
            k2= "It's raining but water level is LOW!!!"
            print k2
            print k1
            finally_=server+k2
            f = urllib.urlopen(finally_)
    else:
        finish=server+"*******No Rain*****"
        f = urllib.urlopen(finish)
        
            
    
