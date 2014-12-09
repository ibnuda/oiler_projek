#!/usr/bin/env python2
# encoding: utf-8

total = 0

for itung in xrange(1,1000):
    if (itung % 3) == 0:
        total += itung
    elif (itung %5) == 0:
        total += itung

print(total)
