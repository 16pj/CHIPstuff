#!/usr/bin/python3

import CHIP_IO.GPIO as GPIO
import warnings

class SevSeg:
	_g="XIO-P0"
	_f="XIO-P1"
	_a="XIO-P2"
	_b="XIO-P3"
	_e="XIO-P4"
	_d="XIO-P5"
	_c="XIO-P6"
	_h="XIO-P7"

	def __init__(self, g=_g, f=_f, a=_a, b=_b, e=_e, d=_d, c=_c, h=_h):
		self.pins = [a,b,c,d,e,f,g,h]
		self.setup(self.pins) 
		return None		

	def setup(self, pins):
		warnings.filterwarnings('ignore')
		for pin in pins:
			GPIO.setup(pin, GPIO.OUT)

	def on(self, pins):
		for pin in pins:	
			GPIO.output(pin, GPIO.HIGH)

	def off(self, pins):
		for pin in pins:
                	GPIO.output(pin, GPIO.LOW)

	def glow_these(self, pins, comp=False):
		notpins = [i for i in self.pins if i not in pins]
		if comp is False:
			self.on(notpins)
			self.off(pins)
		else:
			self.off(notpins)
			self.on(pins)

g="XIO-P0"
f="XIO-P1"
a="XIO-P2"
b="XIO-P3"
e="XIO-P4"
d="XIO-P5"
c="XIO-P6"
h="XIO-P7"

mypins = [a,b,c]
toy = SevSeg(g,f,a,b,e,d,c,h)
toy.glow_these(mypins)
