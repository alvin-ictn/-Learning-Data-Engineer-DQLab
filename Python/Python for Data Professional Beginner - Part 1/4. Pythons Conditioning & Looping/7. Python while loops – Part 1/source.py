# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 05:48:58 2021

@author: Alvin

Tugas 1:
Hitung total tagihan secara manual dengan menulis potongan kode berikut ke dalam live code editor:

Setelah aku konfirmasi potongan kode yang aku buat ke Senja, aku belajar bahwa potongan kode ini tidak efektif apabila ukuran dari list tagihan bertambah. Tentunya aku akan kewalahan untuk menuliskan ekspresi penambahan pada setiap elemennya, terutama jika elemennya berjumlah banyak. Untuk mengatasi hal ini Senja memberikan masukan untuk menggunakan struktur kontrol while.

 

Tugas 2:
Rubah potongan kode yang telah dibuat dengan arahan senja, dan tuliskan di dalam live code editor:



Setelah dijalankan, kedua potongan kode akan mencetak output yang sama yaitu 750000. 

 
"""

# Tagihan
tagihan = [50000, 75000, 125000, 300000, 200000]
# Tanpa menggunakan while loop
total_tagihan = tagihan[0] + tagihan[1] + tagihan[2] + tagihan[3] + tagihan[4]
print(total_tagihan)
# Dengan menggunakan while loop
i = 0 # sebuah variabel untuk mengakses setiap elemen tagihan satu per satu
jumlah_tagihan = len(tagihan) # panjang (jumlah elemen dalam) list tagihan
total_tagihan = 0 # mula-mula, set total_tagihan ke 0
while i < jumlah_tagihan: # selama nilai i kurang dari jumlah_tagihan
    total_tagihan += tagihan[i] # tambahkan tagihan[i] ke total_tagihan
    i += 1 # tambahkan nilai i dengan 1 untuk memproses tagihan selanjutnya.
print(total_tagihan)