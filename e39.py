#!/usr/bin/env python
# encoding: utf-8

"""
jika s adalah panjang sisi dari segitiga siku dengan panjang sisi (integral) 
{a, b, c}, ada tiga solusi untuk p = 120 => 20,48,52 24,45,51 30,40,50
untuk p kurang dari 1000, tentukan jumlah solusi maksimal.
"""

def ngitung_siku_siku(panjang):
    lemper = 0
    for sisi_a in xrange(1, panjang + 1):
        for sisi_b in xrange(sisi_a, panjang + 1):
            sisi_c = panjang - sisi_a - sisi_b
            if (sisi_b <= sisi_c and
                sisi_a ** 2 + sisi_b ** 2 == sisi_c ** 2):
                lemper += 1
    return lemper

maks = 0
for panjang in xrange(1, 1001):
    maks_sem = ngitung_siku_siku(panjang)
    if maks_sem > maks:
        panjang_pol = panjang
        maks = maks_sem

print(panjang_pol)
