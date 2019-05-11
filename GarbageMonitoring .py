import os
import time
import RPi.GPIO as GPIO
import urllib2
import urllib
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
TRIG1 = 40 
ECHO1 = 38
TRIG2 = 35 
ECHO2 = 37

GPIO.setup(TRIG1,GPIO.OUT)
GPIO.setup(ECHO1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(TRIG2,GPIO.OUT)
GPIO.setup(ECHO2, GPIO.IN, pull_up_down=GPIO.PUD_UP)

Bin2='https://api.thingspeak.com/update?api_key=U04OZELFSJICEUSU&field2='
#Bin3='https://api.thingspeak.com/update?api_key=U04OZELFSJICEUSU&field3='
#Bin4='https://api.thingspeak.com/update?api_key=U04OZELFSJICEUSU&field4='

def val1() :

  GPIO.output(TRIG1, GPIO.LOW)
  time.sleep(2)
  GPIO.output(TRIG1, GPIO.HIGH)
  time.sleep(0.00001)
  GPIO.output(TRIG1, GPIO.LOW)
  while GPIO.input(ECHO1)==0:
    pulse_start = time.time()
  while GPIO.input(ECHO1)==1:
    pulse_end = time.time()
  pulse_duration = pulse_end - pulse_start
  distance = pulse_duration * 17150
  distance1 = round(distance, 2)
  a=str(distance1)
  #b='https://api.thingspeak.com/update?key=154V2WPYDD17XH9S&field1='
  #b='https://api.thingspeak.com/update?api_key=U04OZELFSJICEUSU&field1='
  Bin1='https://api.thingspeak.com/update?api_key=U04OZELFSJICEUSU&field1='
  url1=Bin1+a
  
  f = urllib.urlopen(url1)
  #print 'data uploadaed.............. '
  print"Bin1:"," ",(a)
def val2() :

  GPIO.output(TRIG2, GPIO.LOW)
  time.sleep(2)
  GPIO.output(TRIG2, GPIO.HIGH)
  time.sleep(0.00001)
  GPIO.output(TRIG2, GPIO.LOW)
  while GPIO.input(ECHO2)==0:
    pulse_start = time.time()
  while GPIO.input(ECHO2)==1:
    pulse_end = time.time()
  pulse_duration = pulse_end - pulse_start
  distance = pulse_duration * 17150
  distance2 = round(distance, 2)
  a=str(distance2)
  #b='https://api.thingspeak.com/update?key=154V2WPYDD17XH9S&field1='
  #b='https://api.thingspeak.com/update?api_key=U04OZELFSJICEUSU&field1='
  Bin2='https://api.thingspeak.com/update?api_key=U04OZELFSJICEUSU&field2='
  url2=Bin2+a
  
  f = urllib.urlopen(url2)
  #print 'data uploadaed.............. '
  print "Bin2:"," ",(a)
  
while True:
  val1()
  time.sleep(5)
  val2()
  print 'data uploadaed.............. '
  time.sleep(10)
 
  
