import RPi.GPIO as GPIO
import time;
import os;
#import Buzzer;

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(3, GPIO.OUT)
GPIO.output(3, 1)
time.sleep(3)
GPIO.output(3, 0)
