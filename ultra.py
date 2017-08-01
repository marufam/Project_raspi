import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)

TRIG = 5
ECHO = 3
#red = 18


print "Distance Measurement In Progress"

GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)
#GPIO.setup(red,GPIO.OUT)
#GPIO.setup(green,GPIO.OUT)
#GPIO.setup(yellow, GPIO.OUT)

GPIO.output(TRIG,False)

while 1:
	print "Waiting For Sensor To Settle"
	time.sleep(0.5)

	GPIO.output(TRIG,True)
	time.sleep(0.5)
	GPIO.output(TRIG,False)

	while GPIO.input(ECHO)==0:
	  pulse_start = time.time()

	while GPIO.input(ECHO)==1:
	  pulse_end = time.time()

	pulse_duration = pulse_end - pulse_start

	distance = (pulse_duration * 34300) / 2

	distance = round(distance,2)

	print "Distance:",distance,"cm"

	#if(distance < 5):
	#	GPIO.output(red, 1)
	#	print "red"
#	elif(5 <= distance < 10):
#		print "green"
#		GPIO.output (green, 1)	
	#else:
	#	print "yellow"
	#	GPIO.output (red, 0)

	time.sleep(0.1)

GPIO.cleanup()
