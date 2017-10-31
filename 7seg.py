#!/usr/bin/python3

import CHIP_IO.GPIO as GPIO

g="XIO-P0"
f="XIO-P1"
a="XIO-P2"
b="XIO-P3"
e="XIO-P4"
d="XIO-P5"
c="XIO-P6"
h="XIO-P7"

pins = [a,b,c,d,e,f,g,h]

def setup(pins):
	for pin in pins:
		GPIO.setup(pin, GPIO.OUT)

def on(pins):
	for pin in pins:	
		GPIO.output(pin, GPIO.HIGH)

def off(pins):
	for pin in pins:
                GPIO.output(pin, GPIO.LOW)

mypins = [a,b,c]
notmypins = [i for i in pins if i not in mypins]

setup(pins)
on(notmypins)
off(mypins)


