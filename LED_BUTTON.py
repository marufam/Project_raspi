import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(8, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(3,GPIO.OUT)
counter = 0
try:
	#counter=0
	while True:
		button_state = GPIO.input(8)
		if button_state == False and counter == 0:
			#if counter==0 and GPIO.output(3)==LOW:
			print "LED on"
			GPIO.output(3,1)
			#print "Button pressed"
			#time.sleep(1)
			counter=1
		if button_state == False and counter == 1:
			GPIO.output(3,0)
			print "LED off"
			#time.sleep(1)
			counter=0
			print "button not pressed"
		else:
			GPIO.output(3,0)
			print "mati"
except:
	GPIO.cleanup()
