from time import sleep
import RPi.GPIO as GPIO       ## Import GPIO library
import serial
import os
import urllib2
import cookielib
from getpass import getpass
import sys
from stat import *
from urllib import urlencode
import telepot
from telepot.loop import MessageLoop
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)      ## Use board pin numbering
m1a=32
m1b=36
m2a=37
m2b=38
ir1=29
ir2=31
ir3=33
ir4=35
HIGH=1
LOW=0
GPIO.setup(ir1, GPIO.IN)            # initialize GPIO Pin as outputs
GPIO.setup(ir2, GPIO.IN)            # initialize GPIO Pin as input
GPIO.setup(ir3, GPIO.IN)            # initialize GPIO Pin as outputs
GPIO.setup(ir4, GPIO.IN)            # initialize GPIO Pin as input

GPIO.setup(m1a, GPIO.OUT)      ## Setup GPIO Pin 11 to OUT
GPIO.setup(m1b, GPIO.OUT)
GPIO.setup(m2a, GPIO.OUT)
GPIO.setup(m2b, GPIO.OUT)
#GPIO.output(led, HIGH)
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
def motor1(Dir):
    if Dir=="clock":
        GPIO.output(m1a,GPIO.HIGH)  
        GPIO.output(m1b,GPIO.LOW)
        print"clock"
        
    elif Dir=="aclock":
        GPIO.output(m1a,GPIO.LOW)  
        GPIO.output(m1b,GPIO.HIGH)
        print"anti-clock"
        #break
    
def motor2(Dir):
    if Dir=="clock":
        GPIO.output(m2a,GPIO.HIGH)  
        GPIO.output(m2b,GPIO.LOW)
        print"clock2"
        #break
    elif Dir=="aclock":   
        GPIO.output(m2a,GPIO.LOW)  
        GPIO.output(m2b,GPIO.HIGH)
        print"anti-clock2"
        #break
            

def m1stop():
    GPIO.output(m1a,GPIO.LOW)  
    GPIO.output(m1b,GPIO.LOW)
    print"gate 1 closed"
def m2stop():
    GPIO.output(m2a,GPIO.LOW)  
    GPIO.output(m2b,GPIO.LOW)
    print"gate 2 closed"


#GPIO.setwarnings(False)
#GPIO.setmode(GPIO.BCM)
def gate1IN():
    if GPIO.input(ir1)==1:
        motor1("clock")
        print "gate1 opened"
        sleep(4)
        m1stop()
        sleep(3)
        motor1("aclock")
        print "gate1 closed"
        sleep(4)
        m1stop()

def gate1OUT():
    if GPIO.input(ir2)==1:
        motor1("clock")
        print "gate1 opened"
        sleep(4)
        m1stop()
        sleep(3)
        motor1("aclock")
        print "gate1 closed"
        sleep(4)
        m1stop()
        
def gate2IN():
    if GPIO.input(ir3)==1:
        motor2("clock")
        print "gate2 opened"
        sleep(4)
        m2stop()
        sleep(3)
        motor2("aclock")
        print "gate2 closed"
        sleep(4)
        m2stop()

def gate2OUT():
    if GPIO.input(ir4)==1:
        motor2("clock")
        print "gate2 opened"
        sleep(4)
        m2stop()
        sleep(3)
        motor2("aclock")
        print "gate2 closed"
        sleep(4)
        m2stop()
def gate1INBLOCK():
    m1stop()
def gate2INBLOCK():
    m2stop()

def slot1Full():
    if GPIO.input(ir1)==1:
        sleep(1)
        if GPIO.input(ir2)==1:
            print "slot 1 Full"
            sms("slot 1 full")
    
def slot1Empty():
    if GPIO.input(ir2)==1:
        sleep(1)
        if GPIO.input(ir1)==1:
            print "slot 1 Empty"
            sms("slot 1 Empty")

def slot2Full():
    if GPIO.input(ir3)==1:
        sleep(1)
        if GPIO.input(ir4)==1:
            print "slot 2 Full"
            sms("slot 2 full")
    
def slot1Empty():
    if GPIO.input(ir4)==1:
        sleep(1)
        if GPIO.input(ir3)==1:
            print "slot 2 Empty"
            sms("slot 2 Empty")
##def action(msg):
##    chat_id = msg['chat']['id']
##    command = msg['text']
##    print 'Received: %s' % command
##    if "Status" in command:
##        message = message + "Welcome to the world of automated parking"
##        telegram_bot.sendMessage (chat_id, message)
##        if slot1Empty() and slot2Empty() == True:
##            message = message + "all slots Empty"
##            telegram_bot.sendMessage (chat_id, message)
##        elif slot1Empty() == True:
##            message = message + "all slot1 Empty"
##            telegram_bot.sendMessage (chat_id, message)
##            if "Block" in command:
##                gate1INBLOCK()
##                message = message + "blocked"
##                telegram_bot.sendMessage (chat_id, message)
##                
##        elif slot2Empty() == True:
##            message = message + "all slot2 Empty"
##            telegram_bot.sendMessage (chat_id, message)
##            if "Block" in command:
##                message = message + "blocked"
##                telegram_bot.sendMessage (chat_id, message)                
##        elif slot1Full() == True:
##            message = message + "all slot1 Full"
##            telegram_bot.sendMessage (chat_id, message)
##        elif slot2Full() == True:
##            message = message + "all slot2 Full"
##            telegram_bot.sendMessage (chat_id, message)
##        elif slot1Empty() or slot2Empty() == True:
##            message = message + "all slots Empty"
##            telegram_bot.sendMessage (chat_id, message)
##telegram_bot = telepot.Bot('490931620:AAEbUczl-ptZWqo57XKebYEA4B-hhYTDN78')
##print (telegram_bot.getMe())
##MessageLoop(telegram_bot, action).run_as_thread()
##print 'Up and Running....'                    
##    
            
            
            
def main_loop():
    slot1Full()
    slot2Full()
    slot1Empty()
    slot1Empty()
    gate1IN()
    gate1OUT()
    gate2IN()
    gate2OUT()
    
   
    
while True:
    main_loop()
    
    
