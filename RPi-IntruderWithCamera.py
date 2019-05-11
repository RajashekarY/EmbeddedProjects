import RPi.GPIO as gpio
import picamera
import time

import smtplib
from email.MIMEMultipart import MIMEMultipart 
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email import encoders
from email.mime.image import MIMEImage

fromaddr = "piotcamera@gmail.com"    # change the email address accordingly
toaddr = "leenakatari847@gmail.com"
 
mail = MIMEMultipart()
 
mail['From'] = fromaddr
mail['To'] = toaddr
mail['Subject'] = "Security Alert"
body = "Security Alert, Check the Below Attachment"

buz=20
pir=21
HIGH=1
LOW=0
gpio.setwarnings(False)
gpio.setmode(gpio.BCM)
gpio.setup(buz, gpio.OUT)            # initialize GPIO Pin as outputs
gpio.setup(pir, gpio.IN)            # initialize GPIO Pin as input
data=""
def buzzer(k):
    for i in range(0,k):
        gpio.output(buz, 1)
        time.sleep(0.2)
        gpio.output(buz, 0)
        time.sleep(0.1)
        
buzzer(3)        
    
def sendMail(data):
    mail.attach(MIMEText(body, 'plain'))
    print data
    dat='%s.jpg'%data
    print dat
    attachment = open(dat, 'rb')
    image=MIMEImage(attachment.read())
    attachment.close()
    mail.attach(image)
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromaddr, "piCAMERA")
    text = mail.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()

def capture_image():
    data= time.strftime("%d_%b_%Y|%H:%M:%S")
    #camera.start_preview()
    #time.sleep(.1)
    print data
    camera.capture('%s.jpg'%data)
    #camera.stop_preview()
    #time.sleep(0.1)
    sendMail(data)

gpio.output(buz , 0)
camera = picamera.PiCamera()
camera.rotation=180
camera.awb_mode= 'auto'
camera.brightness=55
while 1:
    if gpio.input(pir)==1:
        gpio.output(buz, 1)
        time.sleep(.2)
        gpio.output(buz, 0)
        print 'some one present'
        capture_image()
        buzzer(15)
        while(gpio.input(pir)==1):
            time.sleep(1)
        
    else:
        pass
        
        
