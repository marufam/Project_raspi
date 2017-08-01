import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(8, GPIO.IN)

for i in range(0,5):
	print GPIO.input(8)
