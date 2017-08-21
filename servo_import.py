import RPi.GPIO as GPIO
import time
import requests as requests
import json as json

GPIO.setmode(GPIO.BOARD)
GPIO.setup(13, GPIO.OUT)
p = GPIO.PWM(13, 50)
p.start(2.5)

def open():
	p.ChangeDutyCycle(5.5)
		#print stat
		#break
#p.stop()

def close():
	p.ChangeDutyCycle(2.5)
		#print stat
		#break
while 1:
	r = requests.get('http://10.42.0.1/raspi_api/index.php/Tool_api')
	stat=r.json()['tools'][4]['status']
	if(stat=='1'):
		open()
		time.sleep(1)
	else:
		close()
		time.sleep(1)
	#p.stop()
#	time.sleep(1)
#	p.ChangeDutyCycle(25.0)
#	time.sleep(1)
#except KeyboardInterrupt:
#	p.stop()
#	GPIO.cleanup()
