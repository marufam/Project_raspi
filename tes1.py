import RPi.GPIO as GPIO
import time
import os
import buzzer

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(4, GPIO.OUT)
GPIO.output(4, 1)
print("YOLO buzzer")