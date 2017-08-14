import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(13, GPIO.OUT)
p = GPIO.PWM(13, 50)
p.start(2.5)

def open():
	p.ChangeDutyCycle(5)
		#print stat
		#break
#p.stop()

def close():
	p.ChangeDutyCycle(2.5)
		#print stat
		#break
#while 1:
#	open()
#	close()
	#p.stop()
#	time.sleep(1)
#	p.ChangeDutyCycle(25.0)
#	time.sleep(1)
#except KeyboardInterrupt:
#	p.stop()
#	GPIO.cleanup()
