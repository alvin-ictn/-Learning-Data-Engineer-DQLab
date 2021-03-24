# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 21:54:27 2021

@author: Alvin

Tugas Praktek
“Saya lihat kamu cepat belajar. Gimana kalau kamu coba buat kalkulator sederhana untuk potongan harga dan pajak, Aksara?” komentar Senja padaku.


Tugas:
Aku diminta menghitung harga_setelah_potongan dan harga_final dengan mengalikan harga_setelah_potongan dengan angka 1.1 karena jumlah PPN sebesar 10% (100% + 10% = 110% atau 1.1)
Aku menggunakan variabel harga_asli dengan nilai 20000 dan variabel potongan dengan nilai 2000.
"""

harga_asli = 20000
potongan = 2000
harga_setelah_potongan = harga_asli - potongan
harga_final = harga_setelah_potongan * 1.1
print(harga_final)