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
