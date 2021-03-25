# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 17:19:58 2021

@author: Alvin

DUseful Tips and Tricks
Untuk menentukan berapa jumlah data yang tersimpan di setiap elemen pada tuple/list, aku dapat menggunakan fungsi buit-in len(). 


Tugas 1:
Ketikkan potongan kode berikut pada live code editor:



akan menghasilkan output 4. Kemudian,



akan menghasilkan output 4.

Tugas 2:
Ternyata ada trik khusus yang dapat aku gunakan untuk mengkonversi berbagai tipe data collection. Contohnya:


Selanjutnya aku dapat melemparkan list ke dalam set() untuk mengkonversi sebuah list ke sebuah set


dan melemparkan set ke dalam list() untuk mengkonversi sebuah set ke sebuah list


akan menampilkan output:


trik ini akan sangat berguna ketika aku ingin mendapatkan seluruh list element unik pada bahasa pemrograman Python.

 

 

Tugas:
Ketikkan potongan kode berikut pada live code editor:
"""
# Tuple
print(">>> Tuple")
tuple_menu = ('Gado-gado','Ayam Goreng','Rendang','Ketoprak')
jumlah_menu = len(tuple_menu)
print(jumlah_menu)
# List
print(">>> List")
list_menu = ['Gado-gado','Ayam Goreng','Rendang','Ketoprak']
jumlah_menu = len(list_menu)
print(jumlah_menu)
# Konversi tipe data
print(">>> Konversi tipe data")
list_buah = ['Apel', 'Apel', 'Jeruk', 'Markisa', 'Jeruk', 'Markisa', 'Apel']
set_buah = set(list_buah)
print(set_buah)
list_buah = list(set_buah)
list_buah.sort()
print(list_buah)