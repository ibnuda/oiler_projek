#!/usr/bin/env python2
# encoding: utf-8

def fak(x, s=1):
    s *= x
    if x > 1:
        return fak(x-1, s)
    else:
        return s

def ngekek(tulisan):
    total = 0
    tulisan = list(tulisan)
    for anu in tulisan:
        total += int(anu)
    return total

asuDawaBangetAnune = str(fak(100))

print(ngekek(asuDawaBangetAnune))
