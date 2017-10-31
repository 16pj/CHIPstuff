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
		
		self.a=a
		self.b=b
		self.c=c
		self.d=d
		self.e=e
		self.f=f
		self.g=g
		self.h=h
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

	# Numbers
	def digit(self, digit=7):
		if digit == 1 or digit == '1':
			self.glow_these([self.b, self.c])
		elif digit == 2 or digit == '2':
                        self.glow_these([self.a, self.b, self.g, self.e, self.d])
		elif digit == 3 or digit == '3':
                        self.glow_these([self.a, self.b, self.g, self.c, self.d])
		elif digit == 4 or digit == '4':
                        self.glow_these([self.f, self.b, self.g, self.c])
		elif digit == 5 or digit == '5':
                        self.glow_these([self.a, self.f, self.g, self.c, self.d])
		elif digit == 6 or digit == '6':
                        self.glow_these([self.f, self.a, self.c, self.g, self.e, self.d])
		elif digit == 7 or digit == '7':
                        self.glow_these([self.a, self.b, self.c])
		elif digit == 8 or digit == '8':
			self.glow_these([self.a, self.b, self.c, self.d, self.e, self.f, self.g])
		elif digit == 9 or digit == '9':
			self.glow_these([self.a, self.b, self.g, self.f, self.c])
		elif digit == 0 or digit == '0':
			self.glow_these([self.a, self.b, self.c, self.d, self.e, self.f])
		else:
			self.glow_these([self.h])
		return None
