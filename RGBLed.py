import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(3, GPIO.OUT)
GPIO.setup(5, GPIO.OUT)
GPIO.setup(7, GPIO.OUT)

while 1:
	GPIO.output(3,1)
	GPIO.output(5,0)
	GPIO.output(7,0)
	time.sleep(1)
	GPIO.output(3,0)
	GPIO.output(5,1)
	GPIO.output(7,0)
	time.sleep(1)
	GPIO.output(3,0)
	GPIO.output(5,0)
	GPIO.output(7,1)
	time.sleep(1)

