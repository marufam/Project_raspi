import RPi.GPIO as GPIO
import time
import subprocess
import urllib
import urllib2
import requests

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(40, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(16,GPIO.OUT)
url = 'http://10.42.0.1/raspi_api/index.php/Guest_api'

while True:
	button_state = GPIO.input(40)
	#print button_state
	if(button_state==0):
		GPIO.output(16, 1)
		time.sleep(1)
		GPIO.output(16, 0)
		subprocess.call(['fswebcam','image.jpg'])
		files = {'location': open('image.jpg','rb')}
		param = {'id':'1', 'status':'0'}
		requests.post(url, files=files, data=param)
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
	else:
		GPIO.output(16, 0)

