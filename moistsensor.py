import RPi.GPIO as GPIO
import Adafruit_DHT as dht
import time;
import os;
import urllib

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)

while True:
    h, t = dht.read_retry(dht.DHT11, 4)
    os.system('date')
    print('temp={0:0.1f}*C hum:{1:0.1f}%'.format(t, h))
    url="http://localhost/splash2/process.php?h="+str(h)+"&t="+str(h)
    response = urllib.urlopen(url).read()
    print(response)
    time.sleep(10)

   # if (t > 30):
    #    GPIO.output(17, GPIO.HIGH)
    #elif (t < 30):
     #   GPIO.output(17, GPIO.LOW)
