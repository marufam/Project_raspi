import RPi.GPIO as GPIO ## Import GPIO library
import time ## Import 'time' library. Allows us to use 'sleep'
import requests as requests
import json as json
GPIO.setmode(GPIO.BOARD) ## Use board pin numbering
GPIO.setup(8, GPIO.OUT) ## Setup GPIO Pin 7 to OUT
GPIO.setup(10, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
##Define a function named Blink()
#def Blink(numTimes,speed):
#	for i in range(0,numTimes):## Run loop numTimes
#		print "Iteration " + str(i+1)## Print current loop
#		time.sleep(speed)## Wait
#		GPIO.output(3,False)## Switch off pin 7
#		time.sleep(speed)## Wait
	#print "Done" ## When loop is complete, print "Done"
	#GPIO.cleanup()
#speed = raw_input("Enter length of each blink(seconds): ")

## Ask user for total number of blinks and length of each blink
#iterations = raw_input("Enter total number of times to blink: ")
while 1:
	r = requests.get('http://10.42.0.1/raspi_api/index.php/Tool_api')
	#data = json.load(r)
	for i in range(0, len(r.json()['tools'])):
		#print r.json()['tools'][i]['name']
		gpio = int(r.json()['tools'][i]['gpio'])
		if(r.json()['tools'][i]['status']=='1'):
			print i
			
			#if(i==0):
			#	print "haha"
			GPIO.output(gpio,True)## Switch on pin 7
			#elif(i==1):
			#	GPIO.output(5, True)			
		else:
			#if(i==0):
			#	print "12"
			GPIO.output(gpio,False)## Switch on pin 7
			#elif(i==1):
			#	GPIO.output(5,False)
		#time.sleep(1)
## Start Blink() function. Convert user input from strings to numeric data types and pass to Blink() as parameters
