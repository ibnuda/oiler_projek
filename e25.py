#!/usr/bin/env python2
# encoding: utf-8

satu = 1
duwa = 1
waow = 1

while True:
    if len(str(satu)) >= 1000:
        break
    satu += duwa
    waow += 1
    if len(str(duwa)) >= 1000:
        break
    duwa += satu
    waow += 1

print(waow)
