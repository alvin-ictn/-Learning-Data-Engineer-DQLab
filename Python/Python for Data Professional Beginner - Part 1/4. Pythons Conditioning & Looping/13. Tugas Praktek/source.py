# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 05:48:58 2021

@author: Alvin

Tugas Praktek
Aku di informasikan Senja bahwa manajemen cukup puas dengan hasil kalkulator potongan harga dan pajak yang aku kembangkan dan aku diberikan kepercayaan lebih untuk membuat program baru.

Dalam program kali ini, aku diminta untuk menghitung total pengeluaran dan pemasukan perusahaan.

Senja pun mengingatkan akan ada penghitungan cash flow.

Melihat Senja dan tim manajemen memberikan kepercayaan yang besar kepadaku, akupun bersemangat!


Tugas:
Program yang akan aku bangun akan mengolah sebuah list yang bernama list_cash_flow. Setiap elemen dari list_cash_flow berisikan pengeluaran (bilangan negatif) dan pemasukan (bilangan positif) pada perusahaan

Dari list_cash_flow ini, aku akan menghitung total_pengeluaran dan total_pemasukan perusahaan.

"""

list_cash_flow = [
2500000, 5000000, -1000000, -2500000, 5000000, 10000000,
-5000000, 7500000, 10000000, -1500000, 25000000, -2500000
]
total_pengeluaran, total_pemasukan = 0, 0
for dana in list_cash_flow:
    if dana > 0:
        total_pemasukan += dana
    else:
        total_pengeluaran += dana
total_pengeluaran *= -1
print(total_pengeluaran) 
print(total_pemasukan)