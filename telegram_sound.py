import sys
import time
import random
import datetime
import telepot
import RPi.GPIO as GPIO
from ultra_function import jarak
#LED
def on(pin):
        GPIO.output(pin,GPIO.HIGH)
        return
def off(pin):
        GPIO.output(pin,GPIO.LOW)
        return
# to use Raspberry Pi board pin numbers
GPIO.setmode(GPIO.BOARD)
# set up GPIO output channel
GPIO.setup(3, GPIO.OUT)

def handle(msg):
    chat_id = msg['chat']['id']
    command = msg['text']
    print chat_id
    print 'Got command: %s' % command
	
	
    while 1:
	command = msg['text']
	print command
	if command=='on':
	#on(3)
		jar = jarak(3,5,1)
		print jar       	
		bot.sendMessage(chat_id, jar)
	if command =='off':
		bot.sendMessage(chat_id, "off")
	if jar<10:
		break
		
bot = telepot.Bot('387123027:AAHexo4EFHlLY1GpQMmyrJ1af901jDXgvs0')
bot.message_loop(handle)
print 'I am listening...'

while 1:
     time.sleep(1)
#time.sleep(1)
#jar1 = jarak(3,5,1)
#print jar1
