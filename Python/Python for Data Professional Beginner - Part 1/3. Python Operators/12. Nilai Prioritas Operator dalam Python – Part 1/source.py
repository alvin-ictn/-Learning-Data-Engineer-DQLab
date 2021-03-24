# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 21:54:27 2021

@author: Alvin

Tugas:
Aku diminta Senja untuk menghitung harga yang harus dibayarkan menggunakan barang senilai 150,000, dengan diskon 30% dan pajak 10%, menggunakan cara yang aku gunakan awal, dan cara lebih singkat yang diajarkan Senja. 

 
"""

# Kode awal
total_harga = 150000
potongan_harga = 0.3
pajak = 0.1 # pajak dalam persen ~ 10%
harga_bayar = 1 - 0.3 # baris pertama
harga_bayar *= total_harga # baris kedua
pajak_bayar = pajak * harga_bayar # baris ketiga
harga_bayar += pajak_bayar # baris ke-4
print("Kode awal - harga_bayar=", harga_bayar)
# Penyederhanaan baris kode dengan menerapkan prioritas operator
total_harga = 150000
potongan_harga = 0.3
pajak = 0.1 # pajak dalam persen ~ 10%
harga_bayar = (1 - 0.3) * total_harga #baris pertama 
harga_bayar += harga_bayar * pajak # baris kedua
print("Penyederhanaan kode - harga_bayar=", harga_bayar)