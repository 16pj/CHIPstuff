#!/usr/bin/python3
# Script to call led.py and change two leds at different rates
# Requires two switches or analog inputs
# python3 input.py

import CHIP_IO.GPIO as GPIO
import warnings
import time
from subprocess import Popen

#Connections
led1="XIO-P4"
led2="XIO-P5"
in1="CSID0"
in2="CSID1"
sw="CSID2"

# Setup pins
warnings.filterwarnings('ignore')
GPIO.setup(in1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(in2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(sw, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


if __name__=='__main__':

	l1_speed = 1
	l2_speed = 1
	l1_store = l1_speed
	l2_store = l2_speed
	x = 0
	y = 0
	sub1 = Popen('python3 led.py {0} {1}'.format(led1, 1), shell=True)
	sub2 = Popen('python3 led.py {0} {1}'.format(led2, 1), shell=True)

	while True:
		if GPIO.input(in1):
			a = "x-"
		else:
			a = "x+"
			if GPIO.input(sw):
				l1_speed += 1
			else:
				l1_speed -= 1

		if GPIO.input(in2):
			b = "y-"
		else:
			b = "y+"
			if GPIO.input(sw):
				l2_speed += 1
			else:
				l2_speed -= 1

		print ("{0}, {1}".format(a,b))
		print ("l1-speed {0}, l2-speed {1}".format(l1_speed, l2_speed))
		time.sleep(1)

		if l1_store != l1_speed:
			if l1_speed < 1:
				l1_speed = 1;
			l1_store = l1_speed
			try:
				sub1.kill()
			except:
				pass
			sub1 = Popen('python3 led.py {0} {1}'.format(led1, l1_speed), shell=True)

		if l2_store != l2_speed:
			if l2_speed < 1:
				l2_speed = 1;
			l2_store = l2_speed
			try:
				sub2.kill()
			except:
				pass
			sub2 = Popen('python3 led.py {0} {1}'.format(led2, l2_speed), shell=True)
				     


