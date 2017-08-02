import RPi.GPIO as GPIO
import time;
import os;
#import Buzzer;

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(8, GPIO.OUT)
GPIO.output(8, 1)
time.sleep(3)
GPIO.output(8, 0)
