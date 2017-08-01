import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)

#TRIG = 3
#ECHO = 5
#red = 18


def jarak(TRIG, ECHO, DURASI):

	GPIO.setup(ECHO,GPIO.IN)

	GPIO.setup(TRIG,GPIO.OUT)
	GPIO.output(TRIG,False)

	time.sleep(0.5)

	GPIO.output(TRIG,True)
	time.sleep(DURASI)
	GPIO.output(TRIG,False)

	while GPIO.input(ECHO)==0:
	  pulse_start = time.time()

	while GPIO.input(ECHO)==1:
	  pulse_end = time.time()

	pulse_duration = pulse_end - pulse_start

	distance = (pulse_duration * 34300) / 2

	distance = round(distance,2)

	return distance
