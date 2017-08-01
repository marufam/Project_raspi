import RPi.GPIO as GPIO
import json, requests
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(3, GPIO.OUT)
url = 'http://172.16.48.56/iot/index.php/iot_api'
while 1:
	resp = requests.get(url=url)
	data = json.loads(resp.text)
	if(data['lampu'][0]['status']=="1"):
		GPIO.output(3,1)
	else:
		GPIO.output(3,0)
