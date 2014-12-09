#!/usr/bin/env python2
# encoding: utf-8

def palin(asu):
    men = 0
    mak = len(asu) - 1
    while True:
        if men > mak:
            return True
        a = asu[men]
        b = asu[mak]
        if a != b:
            return False
        men += 1
        mak -= 1

tersangka = 0

""" oke. bruteforce. -_- """
for bangsat in xrange(100,1000):
    for lompya in xrange(100,1000):
        hadeuh = bangsat * lompya
        if palin(str(hadeuh)) and hadeuh > tersangka:
            tersangka = hadeuh

print(tersangka)
