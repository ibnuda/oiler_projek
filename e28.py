#!/usr/bin/env python2
# encoding: utf-8

"""

43 44 45 46 47 48 49
42 21 22 23 24 25 26
41 20  7  8  9 10 27
40 19  6  1  2 11 28
39 18  5  4  3 12 29
38 17 16 15 14 13 30
37 36 35 34 33 32 31

pojok kanan atas  = sisi kuadrat.
pojok kiri  atas  = sisi kuadrat dikurangi sisi ditambah satu
pojok kiri  bawah = sisi kuadrat dikurangi dua sisi ditambah dua
pojok kanan bawah = sisi kuadrat dikurangi tiga sisi tambah tiga
"""

#nge-pur. soalnya (satu kali satu) cuman satu anggota. ._.
total = 1

for sisi in xrange(3, 1002, 2):
    total += sisi * sisi
    total += sisi * sisi - sisi + 1
    total += sisi * sisi - 2 * sisi + 2
    total += sisi * sisi - 3 * sisi + 3

print(total)
