import sys
import time
import random
import datetime
import telepot
import RPi.GPIO as GPIO

#def on(pin):
#       GPIO.output(pin,GPIO.HIGH)
#        return
#def off(pin):
#        GPIO.output(pin,GPIO.LOW)
#        return
# to use Raspberry Pi board pin numbers
GPIO.setmode(GPIO.BOARD)
# set up GPIO output channel
GPIO.setup(3, GPIO.IN)
GPIO.setup(8, GPIO.OUT)

def handle(msg):
    chat_id = msg['chat']['id']
    command = msg['text']
    print chat_id
    print 'Got command: %s' % command
    print GPIO.input(3)
    #if command == '/on':
#	on(3)       	
#    while 1:
    #if(GPIO.input(3)):		
    bot.sendMessage(chat_id, 'intruder')
#	bot.sendPhoto(chat_id, 's.imgur.com/images/logo-1200-630.jpg?2')
    bot.sendPhoto(chat_id, open('image.jpg'))
    GPIO.output(8,1)
    time.sleep(0.5)
    GPIO.output(8,0)
#   elif command =='off':
#       	off(3)
	#bot.sendMessage(chat_id, off(3))
	
bot = telepot.Bot('413174490:AAH8Jy7QU58TFfgvwP8WDIiNJXhiZsy2be4')
while True:
	if GPIO.input(3)==0:
		bot.message_loop(handle)

print 'I am listening...'
print GPIO.input(3)
while 1:
     time.sleep(1)
