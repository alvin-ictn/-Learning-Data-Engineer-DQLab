# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 05:48:58 2021

@author: Alvin

Untuk perintah for loops, aku mencoba potongan kode ini menggunakan live code editor.

 

Jika dijalankan maka akan mencetak output total tagihan sebesar 550000 (total tagihan positif).
"""

list_tagihan = [50000, 75000, -150000, 125000, 300000, -50000, 200000]
total_tagihan = 0
for tagihan in list_tagihan: # untuk setiap tagihan dalam list_tagihan
    total_tagihan += tagihan # tambahkan tagihan ke total_tagihan
print(total_tagihan)