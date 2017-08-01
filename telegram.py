import sys
import time
import random
import datetime
import telepot
import RPi.GPIO as GPIO

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

    if command == 'on':
	on(3)       	
	bot.sendMessage(chat_id, 'on(3)')
    elif command =='off':
       	off(3)
	#bot.sendMessage(chat_id, off(3))

bot = telepot.Bot('387123027:AAHexo4EFHlLY1GpQMmyrJ1af901jDXgvs0')
bot.message_loop(handle)
print 'I am listening...'

while 1:
     time.sleep(1)
