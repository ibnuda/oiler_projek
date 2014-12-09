#!/usr/bin/env python2
# encoding: utf-8

from math import floor

itung = 0
itungan = 0
balik = 0
phi = (1 + 5**0.5) / 2 

""" fug! i want to calculate the value of nth number of fibs """
def fibpangn(x):
    kembalian = floor((phi**x + (1/phi)**x) / 5**0.5)
    return kembalian

while itungan < 4000000:
    if (itungan % 2) == 0:
        balik += itungan
    itungan = fibpangn(itung)
    print(itungan)
    itung += 1

print(balik)

