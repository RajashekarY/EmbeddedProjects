import time, datetime
import RPi.GPIO as GPIO
import telepot
from telepot.loop import MessageLoop
PIR = 36
TEMP = 38
IR = 40
m1a = 35
m1b = 37
Buz = 16

now = datetime.datetime.now()
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
 
 

GPIO.setup(PIR, GPIO.IN)

GPIO.setup(TEMP, GPIO.IN)


GPIO.setup(IR, GPIO.IN)
GPIO.setup(m1a, GPIO.OUT)
GPIO.setup(m1b, GPIO.OUT)
GPIO.output(m1a, GPIO.LOW)
GPIO.output(m1b, GPIO.LOW)

GPIO.setup(Buz,GPIO.OUT)

        
        #GPIO.output(led, HIGH)
        #capture_image()
        #while(GPIO.input(pir)==1):
         #  time.sleep(1)
def action(msg):
    chat_id = msg['chat']['id']
    command = msg['text']
    print 'Received: %s' % command
    if 'start' in command:
        message = "Welcome to the world of automation"
        telegram_bot.sendMessage (chat_id, message)    
        if GPIO.input(PIR)==1:
            message = message + "Someone at yor door"
            telegram_bot.sendMessage (chat_id, message)
            if "ok" in command:
                GPIO.output(m1a, GPIO.HIGH)
                GPIO.output(m1b, GPIO.LOW)
            else:
                pass
        if GPIO.input(TEMP)==1:
            message = message + "HIGH TEMPRATURE AT YOUR HOME"
            telegram_bot.sendMessage (chat_id, message)
        if GPIO.input(IR)==1:
            message = message + "Somebody entered your HOME without your authorisation"
            telegram_bot.sendMessage (chat_id, message)
    elif "What's up" in command:
        message="All is Well"
        telegram_bot.sendMessage (chat_id, message)
         
telegram_bot = telepot.Bot('593773366:AAEevHWwBtB08wb-IRrxcGWBwFl7O9png_M')
print (telegram_bot.getMe())
MessageLoop(telegram_bot, action).run_as_thread()
print 'Up and Running....'
while 1:
    time.sleep(10)
