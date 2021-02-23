#Nama : Freany Mellyn Usmany
#Universitas Kristen Duta Wacana

#Soal bersumber dari https://koding.alza.web.id/latihan-soal-percabangan/
'''Berikut adalah beberapa istilah generasi berdasarkan tahun kelahirannya :
Boomer = 1944 - 1964
Generasi X = 1965 - 1979
Generasi Y = 1980 - 1994
Generasi Z = 1995 - 2015

Buat program dimana user diminta untuk menuliskan nama dan tahun kelahirannya, kemudian cetak nama dan generasinya'''

#Input
nama = input("Masukkan nama Anda") #input nama
tahun_lahir = int(input("Masukkan tahun berapa Anda lahir : ")) #input tahun lahir

#Proses
try:
    tl = int(tahun_lahir)
    if tl >=1944 and tl <=1964:
        print(nama, ", berdasarkan tahun lahir Anda tergolong Boomer")
    elif tl >=1965 and tl <=1979:
        print(nama, ", berdasarkan tahun lahir Anda tergolong Generasi X")
    elif tl >=1980 and tl <=1994:
        print(nama, ", berdasarkan tahun lahir Anda tergolong Generasi Y")
    elif tl >=1995 and tl <= 2015:
        print(nama, ", berdasarkan tahun lahir Anda tergolong Generasi Z")

except:
    print("Tahun lahir Anda di luar range")