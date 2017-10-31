#!/usr/bin/python3

import CHIP_IO.GPIO as GPIO
import warnings


class SevSeg:

	# CLASS FOR HANDLING 7 segment display. Default pin connections are as follows.

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

	# Numbers [0-9]
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

	# Characters (attempt)
	def character(self, char='a'):
		if char.lower() == 'a':
                        self.glow_these([self.a, self.b, self.c, self.e,self.f, self.g])
		elif char.lower() == 'b':
			self.glow_these([self.c, self.d, self.e,self.f, self.g])
		elif char.lower() == 'c':
			self.glow_these([self.a, self.d, self.e, self.f])
		elif char.lower() == 'd':
			self.glow_these([self.b, self.c, self.d, self.e, self.g])
		elif char.lower() == 'e':
			self.glow_these([self.a, self.d, self.e, self.f, self.g])
		elif char.lower() == 'f':
			self.glow_these([self.a, self.e, self.f, self.g])
		elif char.lower() == 'g':
			self.glow_these([self.a, self.b, self.c, self.d, self.f, self.g])
		elif char.lower() == 'h':
			self.glow_these([self.c, self.e, self.f, self.g])
		elif char.lower() == 'i':
			self.glow_these([self.b, self.c])
		elif char.lower() == 'j':
			self.glow_these([self.b, self.c, self.d])
		elif char.lower() == 'l':
			self.glow_these([self.d, self.e, self.f])
		elif char.lower() == 'n':
			self.glow_these([self.c, self.d, self.e, self.g])
		elif char.lower() == 'o':
			self.glow_these([self.a, self.b, self.c, self.d, self.e, self.f])
		elif char.lower() == 'p':
			self.glow_these([self.a, self.b, self.e, self.f, self.g])
		elif char.lower() == 'r':
			self.glow_these([self.e, self.g])
		elif char.lower() == 's':
			self.glow_these([self.a, self.c, self.d, self.f, self.g])
		elif char.lower() == 't':
			self.glow_these([self.d, self.e, self.f, self.g])
		elif char.lower() == 'u':
			self.glow_these([self.b, self.c, self.d, self.e, self.f])
		elif char.lower() == 'x':
			self.glow_these([self.b, self.c, self.e, self.f, self.g])
		elif char.lower() == 'y':
			self.glow_these([self.b, self.c, self.d, self.f, self.g])
		elif char.lower() == 'z':
			self.glow_these([self.a, self.b, self.d, self.e, self.g])
		else:
			self.glow_these([self.h])
		return None
