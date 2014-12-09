#!/usr/bin/env python2
# encoding: utf-8

""" asu naif banget """
for angka in xrange(2520, 1000000000, 2520):
    if (angka % 11 == 0 and 
        angka % 12 == 0 and 
        angka % 13 == 0 and 
        angka % 14 == 0 and
        angka % 15 == 0 and
        angka % 16 == 0 and
        angka % 17 == 0 and
        angka % 18 == 0 and
        angka % 19 == 0 and
        angka % 20 == 0):
        print(angka)

