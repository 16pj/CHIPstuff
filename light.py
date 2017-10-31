#!/usr/bin/python3

import CHIP_IO.GPIO as GPIO
import sys
import time

IN=sys.argv[1]

try:
	IN=int(IN)
except:
	print('could not convert to int. Default 1')
	IN = 1

P1="XIO-P7"
P2="XIO-P6"

GPIO.setup(P1, GPIO.OUT)
GPIO.setup(P2, GPIO.OUT)

a=True
while True:
	GPIO.output(P1, a)
	GPIO.output(P2, not a)
	time.sleep(float(1/IN))
	a = not a

