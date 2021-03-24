# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 05:48:58 2021

@author: Alvin

Ternyata, aku belajar bahwa ada istilah nested loops, yaitu pengulangan bersarang. Dengan nested loops, aku dapat mengkombinasikan (menambahkan) struktur pengulangan lain di dalamnya.  Aku mencoba potongan kode di bawah menggunakan live code editor: 

 

Pada saat aku jalankan, maka output yang dihasilkan adalah:

 

 

Klik tombol  untuk melanjutkan.

"""

list_daerah = ['Malang', 'Palembang', 'Medan']
list_buah = ['Apel', 'Duku', 'Jeruk']
for nama_daerah in list_daerah:
    for nama_buah in list_buah:
        print(nama_buah+" "+nama_daerah)