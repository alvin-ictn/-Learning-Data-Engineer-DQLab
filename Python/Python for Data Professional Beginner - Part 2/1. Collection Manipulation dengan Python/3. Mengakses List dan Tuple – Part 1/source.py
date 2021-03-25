# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 17:19:58 2021

@author: Alvin

Mengakses List dan Tuple – Part 1
Seperti yang telah aku pelajari pada module Python for Data Professional Beginner - Part 1, bab “sequence type”, aku dapat mengakses elemen pada suatu list ataupun tuple dengan menggunakan indeks atau semacam nomor urut dari list atau tuple tersebut. Indeks pada suatu tipe data list atau tuple dimulai dari angka 0.

Tugas 1:
Aku mencoba mempraktekkan potongan kode di bawah dengan live code editor:



Untuk menampilkan output Januari dan Juni, yang aku lakukan adalah mengetikkan syntax simple berikut:



Kemudian, untuk mengakses elemen dari belakang pada suatu list/ tuple, aku juga dapat menggunakan indeks negatif pada list/ tuple.

 

Tugas 2:
Untuk menampilkan output Desember dan November, yang aku lakukan adalah mengetikkan syntax simple berikut:

 
"""

bulan_pembelian = ('Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 'Juli', 'Agustus', 'September', 'Oktober', 'November', 'Desember')
print(bulan_pembelian[0])
print(bulan_pembelian[5])
print(bulan_pembelian[-1])
print(bulan_pembelian[-2])