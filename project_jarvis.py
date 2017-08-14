import RPi.GPIO as GPIO ## Import GPIO library
import time ## Import 'time' library. Allows us to use 'sleep'
import requests as requests
import json as json
from servo_import import open, close

GPIO.setmode(GPIO.BOARD) ## Use board pin numbering
GPIO.setup(8, GPIO.OUT) ## Setup GPIO Pin 7 to OUT
GPIO.setup(10, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)
#GPIO.setup(13, GPIO.OUT)
buff=0
#GPIO.setmode(GPIO.BOARD)
GPIO.setup(13, GPIO.OUT)
p = GPIO.PWM(13, 50)
p.start(2.5)

#def open():
 #       p.ChangeDutyCycle(5)
                #print stat
                #break
#p.stop()

#def close():
 #       p.ChangeDutyCycle(2.5)

#close()
while 1:
	r = requests.get('http://10.42.0.1/raspi_api/index.php/Tool_api')
	stat=r.json()['tools'][4]['status']	
	if(stat=='1' and buff==1):
		open()
		buff=0
	elif(stat=='0' and buff==0):
		close()
		buff=1

	for i in range(0, len(r.json()['tools'])-1):
		#print r.json()['tools'][i]['name']
		gpio = int(r.json()['tools'][i]['gpio'])
		if(r.json()['tools'][i]['status']=='1'): #LED
			#print i
			#if(i==0):
			#	print "haha"
			GPIO.output(gpio,True)## Switch on pin 7
			#elif(i==1):
		#elif(r.json()['tools'][4]['status']=='1'):
		#	GPIO.output(5, True)
			#if(GPIO.ouput(13)==False)):
	#		open(stat)
			#time.sleep(1)
			
		#elif(r.json()['tools'][4]['status']=='0'):
			#if(GPIO.ouput(13)==
#			close(stat)
			#time.sleep(1)
		else:
			#if(i==0):
			#	print "12"
			GPIO.output(gpio,False)## Switch on pin 7
			#elif(i==1):
			#	GPIO.output(5,False)
		#time.sleep(1)
## Start Blink() function. Convert user input from strings to numeric data types and pass to Blink() as parameters
