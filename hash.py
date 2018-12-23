import hashlib
import os
import sys
from platform import python_version

# ini kode bokep
N = '\033[0m'
W = '\033[1;37m'
B = '\033[1;34m'
R = '\033[1;31m'
G = '\033[1;32m'
Y = '\033[1;33m'
C = '\033[1;36m'
D = '\033[90m'

if sys.version_info[0] < 3:
        versi = python_version()
        print(R+"lu menggunakan python versi %s gunakan versi 3 keatas" %(versi))
        print(R+"install : pkg install python ")
        print(R+"usage   : python hash.py")
        exit()

print(D+"")
print('''
      ==============================================
      =  ====  ================  =====  ======  ====
      =  ====  ================  =====  ======  ====
      =  ====  ================  =====  ======  ====
      =  ====  ===   ====   ===  =====  ==  ==  ====
      =        ==  =  ==  =  ==    ===  ======    ==
      =  ====  =====  ===  ====  =  ==  ==  ==  =  =
      =  ====  ===    ====  ===  =  ==  ==  ==  =  =
      =  ====  ==  =  ==  =  ==  =  ==  ==  ==  =  =
      =  ====  ===    ===   ===  =  ==  ==  ==    ==
      ==============================================
''')
print("")
print(R+"          ["+Y+"1"+R+"]"+D+" MD5"+R+"             ["+Y+"4"+R+"]"+D+" SHA256")
print(R+"          ["+Y+"2"+R+"]"+D+" SHA1"+R+"            ["+Y+"5"+R+"]"+D+" SHA384")
print(R+"          ["+Y+"3"+R+"]"+D+" SHA224"+R+"          ["+Y+"6"+R+"]"+D+" SHA512")
print("")
print(R+"                     ["+Y+"A"+R+"]"+D+" All")


def md5():
        teks = input(R+"Masukkan teks"+W+" > ")
        hasil = hashlib.md5(teks.encode())
        print("")
        print(C+hasil.hexdigest())
        print("")

def sha1():
        teks = input(R+"Masukkan teks"+W+" > ")
        hasil = hashlib.sha1(teks.encode())
        print("")
        print(C+hasil.hexdigest())
        print("")

def sha224():
        teks = input(R+"Masukkan teks"+W+" > ")
        hasil = hashlib.sha224(teks.encode())
        print("")
        print(C+hasil_object.hexdigest())
        print("")

def sha256():
        teks = input(R+"Masukkan teks"+W+" > ")
        hasil = hashlib.sha256(teks.encode())
        print("")
        print(C+hasil.hexdigest())
        print("")

def sha384():
        teks = input(R+"Masukkan teks"+W+" > ")
        hasil = hashlib.sha384(teks.encode())
        print("")
        print(C+hasil.hexdigest())
        print("")

def sha512():
        teks = input(R+"Masukkan teks"+W+" > ")
        hasil = hashlib.sha512(teks.encode())
        print("")
        print(C+hasil.hexdigest())
        print("")

def all():
        teks = input(R+"Masukkan teks"+W+" > ")
        hasilmd5 = hashlib.md5(teks.encode())
        hasilsha1 = hashlib.sha1(teks.encode())
        hasilsha224 = hashlib.sha224(teks.encode())
        hasilsha256 = hashlib.sha256(teks.encode())
        hasilsha384 = hashlib.sha384(teks.encode())
        hasilsha512 = hashlib.sha512(teks.encode())
        print(B+"MD5    "+W+"= "+C + hasilmd5.hexdigest())
        print("")
        print(B+"SHA1   "+W+"= "+C + hasilsha1.hexdigest())
        print("")
        print(B+"SHA224 "+W+"= "+C + hasilsha224.hexdigest())
        print("")
        print(B+"SHA256 "+W+"= "+C + hasilsha256.hexdigest())
        print("")
        print(B+"SHA384 "+W+"= "+C + hasilsha384.hexdigest())
        print("")
        print(B+"SHA512 "+W+"= "+C + hasilsha512.hexdigest())
        print("")

pilih = input(R+"Pilih "+W+">> ")

if pilih == "1" or pilih == "01":
   md5()
elif pilih == "2" or pilih == "02":
     sha1()
elif pilih == "3" or pilih == "03":
     sha224()
elif pilih == "4" or pilih == "04":
     sha256()
elif pilih == "5" or pilih == "05":
     sha384()
elif pilih == "6" or pilih == "06":
     sha512()
elif pilih == "a" or pilih == "A":
     all()
else:
   print("Pilih yg bener lah goblok!!")

