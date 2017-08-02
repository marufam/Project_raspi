import RPi.GPIO as GPIO
import time as time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(3,GPIO.IN)
input = GPIO.input(3)
while True:
	print input 
	time.sleep(0.5)
# if (GPIO.input(3)):
  #  print("Flame Detected")
   # time.sleep(1)
 # else:
  #  print("Not Detected")
