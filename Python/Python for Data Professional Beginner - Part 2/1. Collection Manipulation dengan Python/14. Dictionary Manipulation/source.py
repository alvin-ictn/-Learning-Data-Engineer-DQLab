# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 17:19:58 2021

@author: Alvin

Dictionary Manipulation
Aku baru saja selesai mengerjakan beberapa kuis latihan ketika Senja mengejutkanku dengan tepukannya di belakang pundakku.

“Lagi apa kamu, Aksara?”

“Ngagetin aja, Nja.”

“Soalnya serius banget. Padahal saya belum kasih intruksi apa-apa buat lanjut hari ini.”

“Hehehe, iya biar cepet selesai dan bisa praktik lagi,” kataku sembari mengacungkan jari telunjuk dan tengah membentuk ‘peace’.

“Kita bakal banyak praktik kok. Sekarang sudah belajar sampai mana?”

Aku menunjukkan subjudul yang sedang kupelajari saat ini: “Dictionary Manipulation” pada Senja.

“Oke, pas banget. Bab ini ada praktiknya, nanti kupandu ya. Bagian string manipulation juga.”

Sembari menunggu Senja membuka laptopnya, aku kembali melanjutkan membaca:

Terakhir, untuk memanipulasi tipe data dictionary.

 

Tugas:
Ketikkan potongan kode berikut pada live code editor:
"""
# Fitur .clear()
print(">>> Fitur .clear()")
info_karyawan = {'nama' : 'Aksara',
                 'nik' : '1211011',
                 'pekerjaan' : 'Data Analyst'}
info_karyawan.clear()
print(info_karyawan)
# Fitur .copy()
print(">>> Fitur .copy()")
info_karyawan1 = {'nama' : 'Aksara',
                  'nik' : '1211011',
                  'pekerjaan' : 'Data Analyst'}
info_karyawan2 = info_karyawan1.copy()
info_karyawan2['nama'] = 'Senja'
info_karyawan2['nik'] = '1211056'
print(info_karyawan1)
print(info_karyawan2)
# Fitur .keys()
print(">>> Fitur .keys()")
info_karyawan = {'nama' : 'Aksara',
                 'nik' : '1211011',
                 'pekerjaan' : 'Data Analyst'}
kunci_akses = list(info_karyawan.keys())
print(kunci_akses)
# Fitur .values()
print(">>> Fitur .values()")
value_dict = list(info_karyawan.values())
print(value_dict)
# Fitur .update()
print(">>> Fitur .update()")
info_karyawan.update({'skillset':['Python', 'R']})
print(info_karyawan)