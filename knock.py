#!/usr/bin/env python
import RPi.GPIO as GPIO
import time

KNOCK_PIN = 3
#SHOCK_PIN = 13

led_status = 1

def setup():
	GPIO.setmode(GPIO.BOARD)
#	GPIO.setup(SHOCK_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
	GPIO.setup(KNOCK_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
	GPIO.setup(7, GPIO.OUT)
	GPIO.output(7,0)

def knock_detected(e):
	print "KNOCK detected!"
	GPIO.output(7,1)
	time.sleep(1)
	GPIO.output(7,0)

#def shock_detected(e):
#	print "SHOCK detected!"

def loop():
#	GPIO.add_event_detect(SHOCK_PIN, GPIO.FALLING, callback=shock_detected, bouncetime=200)
        GPIO.add_event_detect(KNOCK_PIN, GPIO.FALLING, callback=knock_detected, bouncetime=200)
	while True:
		pass

def destroy():
	GPIO.cleanup()

if __name__ == '__main__':
	setup()
	try:
		loop()
	except KeyboardInterrupt:
		destroy()
