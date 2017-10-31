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

def timer(obj, speed=1, stop=10):
        import time
        i=1
        while stop > 0:
                obj.digit(i%10)
                time.sleep(float(1/speed))
                i += 1
                stop -= 1

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
	#toy.character('p')

	# to count for 't' seconds and at 's' speed; timer(obj, speed=s, stop=t)
	timer(toy, speed=3, stop=30)

