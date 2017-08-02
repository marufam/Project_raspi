import RPi.GPIO as GPIO
import time as time
import subprocess 
ObstaclePin = 3
buzzer = 8
#def setup():
GPIO.setmode(GPIO.BOARD)       # Numbers GPIOs by physical location
GPIO.setup(ObstaclePin, GPIO.IN)
GPIO.setup(buzzer, GPIO.OUT)

while 1:
	#print GPIO.input(3)
	if(GPIO.input(3)==1):
		print "intruder"
		subprocess.call(['fswebcam','image.jpg'])
		GPIO.output(buzzer,1)
		time.sleep(1)
		GPIO.output(buzzer,0)
	else:
		
		GPIO.output(buzzer,0)
	#time.sleep(0.5)
#def loop():
#	while True:
##		if (0 == GPIO.input(ObstaclePin)):
#			print "Barrier is detected !"
			

#def destroy():
#	GPIO.cleanup()                     # Release resource

#if __name__ == '__main__':     # Program start from here
##	setup()
#	try:
#		loop()
#	except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
#		destroy()
