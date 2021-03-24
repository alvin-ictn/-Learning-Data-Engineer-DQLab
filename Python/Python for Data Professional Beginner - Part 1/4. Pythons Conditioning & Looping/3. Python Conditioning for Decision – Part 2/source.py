# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 05:48:58 2021

@author: Alvin

Tugas:
Praktekkan kode berikut di live code editor pada baris setelah kode sebelumnya yang telah dibuat.
"""

jam = 13
if jam >= 5 and jam < 12: # selama jam di antara 5 s.d. 12
    print("Selamat pagi!")
elif jam >= 12 and jam < 17: # selama jam di antara 12 s.d. 17
    print("Selamat siang!")
elif jam >= 17 and jam < 19: # selama jam di antara 17 s.d. 19
    print("Selamat sore!")
else: # selain kondisi di atas
    print("Selamat malam!")