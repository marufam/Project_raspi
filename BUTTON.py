import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(8, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(3,GPIO.OUT)
try:
	while True:
		button_state = GPIO.input(8)
		print button_state
		#if button_state == False:
		#	if GPIO.output(3) == LOW:
		#		#print "LED on"
		#		GPIO.output(3,1)
		#		print "BUtton pressed"
		#		#time.sleep(1)
		#	elif GPIO.ouput(3) == HIGH:
		#		GPIO.ouput(3,0)
		#else:
		#	GPIO.output(3,0)
except:
	GPIO.cleanup()
