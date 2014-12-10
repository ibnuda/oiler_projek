#!/usr/bin/env python2
# encoding: utf-8

ss = ''
itungan = 1
while len(ss) < 1000001:
    ss += str(itungan)
    itungan += 1

total = 1
for x in xrange(1, len(ss)):
    if (x == 1 or
        x == 10 or
        x == 100 or
        x == 1000 or
        x == 10000 or
        x == 100000 or
        x == 1000000):
        total *= int(ss[x])

print(total)
