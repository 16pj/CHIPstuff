#!/usr/bin/python3
# Script that glows led at a given rate
# arguments - 1. CHIP pin 2. rate
# python3 led.py XIO-P1 3

import CHIP_IO.GPIO as GPIO
import warnings
import time
import sys
import atexit


try:
	led_pin = sys.argv[1]
	rate = sys.argv[2]
	rate = float(rate)
except:
	print ("Pin info not correct")
	exit(1)

if rate > 50:
	rate = 50

warnings.filterwarnings('ignore')
GPIO.setup(led_pin, GPIO.OUT)

a = 0

def turnoff(pin):
	GPIO.output(pin, 0)

atexit.register(turnoff, led_pin)

while True:
	GPIO.output(led_pin, a % 2)
	time.sleep(1/rate)
	a += 1


