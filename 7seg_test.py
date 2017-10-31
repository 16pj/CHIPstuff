#!/usr/bin/python3
from SevSeg.SevSeg import SevSeg

g="XIO-P0"
f="XIO-P1"
a="XIO-P2"
b="XIO-P3"
e="XIO-P4"
d="XIO-P5"
c="XIO-P6"
h="XIO-P7"

mypins = [a,b,c]
toy = SevSeg(g,f,a,b,e,d)
toy.glow_these(mypins)

if __name__ == '__main__':
	# instantiate with or without pins in given order
	toy = SevSeg(g,f,a,b,e,d)
	
	# create array of pins to glow
	mypins = [a, f, e, d]

	# to glow a set of pins
	#toy.glow_these(mypins)

	# to glow a set of pins without complement
	#toy.glow_these(mypins, comp=True)

	# to display digits from [0-9]
	#toy.digit(7)
	
	# to display characters from [a-z] with missing characters
	import sys
        toy.character(str(sys.argv[1]))
