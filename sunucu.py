import socket
import time
import sys

sunucuSoketi = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
adres = ('')
port = 50000
sunucuSoketi.bind((adres,port))
global baglantiAdedi
baglantiAdedi = 1
sunucuSoketi.listen(1)
print ("\n", port ,  " Portu acildı Istemci bekleniyor...")

def baglanti():
    try:
        print ("\n", baglantiAdedi ,"nolu baglanti bekleniyor")
        global istemci
        istemci, istemciAdresi = sunucuSoketi.accept()
        print ("\n Baglanti Tamam \n İstemci adresi",istemciAdresi)
    except:
        print("\n ÇIKIŞ YAPILIYOR")
        sys.exit()

def verial():
    try:
        gelenVeri = istemci.recv()
        return gelenVeri
    except:
        print ("\nHata Bağlantı Kesildi Yeni Bağlantı Bekleniyor.")
        global baglantiAdedi
        baglantiAdedi += 1
        baglanti()



baglanti()

while True:
    try:      
        deger = verial()
        print("Gelen Veri", deger)
        print("Gelen Verinin Tipi: ",type(deger))
        
        
    except:
        print("\nDöngüden Hata Oluştu")
