import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
while True:
	GPIO.setup(3,GPIO.OUT)
	#print "LED on"
	GPIO.output(3,1)
	time.sleep(1)
	#print "LED off"
	GPIO.output(3,0)
	time.sleep(1)
