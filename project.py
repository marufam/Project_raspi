import RPi.GPIO as GPIO
import Adafruit_DHT as dht
import time  
import os
import urllib

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(37, GPIO.IN)
GPIO.setup(15, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(7, GPIO.OUT)

while True:
	#h, t = dht.read_retry(dht.DHT22,3)
	#os.system('date')
	#print(h)
	#print(t)
#	print('hum:{1:.1f}% temp={0:.1f}*C'.format(h, t))
	#url="http://10.42.0.210/Tea_Pi/Tampildata_c/create/30/20/WAT"
	#url="http://10.42.0.210/Tea_Pi/.php?h="+str(h)+"&t="+str(t)
	#response = urllib.urlopen(url).read()
	#print(response)


        if GPIO.input(37) == 1:
                print("SOIL is DRY")
                GPIO.output(15, 0)
                GPIO.output(13, 0)
		GPIO.output(7, 1)
        else:
                print("SOIL is WET")
                GPIO.output(15, 1)
                GPIO.output(13, 1)
		GPIO.output(7, 0)
        time.sleep(1)




	#if ((GPIO.input(37)) == 1 or (t > 30)):
	#	print("SOIL is DRY")
	#	GPIO.output(15, 0)
	#	GPIO.output(13, 0)
	#else:
	#	print("SOIL is WET")
	#	GPIO.output(15, 1)
	#	GPIO.output(13, 1)
	#time.sleep(1)


