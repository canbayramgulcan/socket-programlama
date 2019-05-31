import socket
import sys
import time

global istemci
import json
sunucu = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
global server_adress
server_adress = ('192.168.x.x') #sunucu ip adresi
global port
port = 50000




def baglanti():
    while True:
        try:
            print("----------------------Baglaniyor----------------------")
            sunucu.connect((server_adress , port))
            print("--------------------Baglanti Tamam--------------------\n")
            break
        except:
            print("--Sunucuya Bağlanılamadı 2 Sn Sonra Tekrar Denenecek--")
            time.sleep(2)

def veriGonder(veri):
    try:
        print("-------------------Veri Yollandı---------------------")
        sunucu.send(str(veri).encode('utf-8'))
    except:
        print("\n*************************HATA*************************",
              "\n**************Sunucu Bağlantısı Kesildi***************",
              "\n*****************Programdan Çıkılıyor*****************",
              "\n******************************************************\n")
        saniye = 5
        while saniye > 0:
              print("*********************",saniye," Sn********************", sep="")
              time.sleep(1)
              saniye -=1
        sys.exit()       

baglanti()

while True:
    try:
        girilenVeri = input()
        print("Gonderilen veri: ",girilenVeri)
        veriGonder(cevrilmis)

    except:
        print("Döngüde Hata")
