#Di coding oleh iFanpS
#Memakai module punya Krypton-Byte (https://github.com/krypton-byte)
#TERIMAKASIH TELAH MEMAKAINYA!

import os, time
try:
    from jagokata import cari_peribahasa
    from jagokata import cari_katabijak
    from art import *
except:
    os.system('pip install jagokata')
    time.sleep(1)
    os.system('pip install art')

def pbhs():
    tprint('\033Peribahasa')
    tanya_kata = input('\033[34mKata yang mau di cari pribahasanya: ')
    try:
        peribahasa = cari_peribahasa(tanya_kata)
        for i in peribahasa:
            type_slowly(f"\033[30mPeribahasanya: \033[32m{i.peribahasa}\n\033[30mArtinya: \033[32m{i.arti}",.03)
            tanya_mau_kembali_atau_tidak = input('Tekan "y" untuk mencari pribahasa, Tekan "N" untuk kembali ke menu awal: ')
            if tanya_mau_kembali_atau_tidak == 'y':
                pbhs()
            elif tanya_mau_kembali_atau_tidak == 'n':
                main_menu()
    except:
        print('\033[91mPribahasa tidak ditemukan!!')
        time.sleep(1.4)
        pbhs()

def ktbjk():
    tprint('\033KataBijak')
    tanya_kata = input('\033[34mKata bijak yang ingin di cari: ')
    try:
        katabijak = cari_katabijak(tanya_kata)
        for i in katabijak:
            type_slowly(f'\033[30mHasil yang di temukan: \033[32m{i.text}', .03)
            tanya_mau_kembali_atau_tidak = input('Tekan "y" untuk mencari pribahasa, Tekan "N" untuk kembali ke menu awal: ')
            if tanya_mau_kembali_atau_tidak == 'y':
                ktbjk()
            elif tanya_mau_kembali_atau_tidak == 'n':
                main_menu()
    except:
        print('\033[91mKatabijak tidak ada hasil!!')
        time.sleep(1.4)
        pbhs()

def type_slowly(text, speed, newLine = True):
    for i in text: 
        print(i, end = "", flush = True) 
        time.sleep(speed) 
    if newLine:
        print() 

def main_menu():
    tprint('JagoKata')
    pilihan = input('\033[34mPeribahasa atau Katabijak: ')
    if pilihan.lower() == 'peribahasa':
        print('\033[32mPeribahasa terpilih, tunggu sebentar...')
        time.sleep(1)
        pbhs()
    elif pilihan.lower() == 'katabijak':
        print('\033[32mKataBijak terpilih, tunggu sebentar...')
        time.sleep(1)
        ktbjk()

if __name__ == "__main__":
    main_menu()
