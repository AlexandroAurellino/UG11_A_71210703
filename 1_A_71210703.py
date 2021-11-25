def calculator():
    print("======== Calculator sederhana ========")
    print("1. Pertambahan")
    print("2. Pengurangan")
    print("3. Perkalian")
    print("4. Pembagian")
    print("5. Pangkat")

    x = int(input("Masukkan pilihan: "))

    if x == 1:
        tambah()
    elif x == 2:
        kurang()
    elif x == 3:
        kali()
    elif x == 4:
        bagi()
    elif x == 5:
        pangkat()
    else:
        print("Hasilnya: Maaf input operasi antara 1-5")

def tambah():
    bil1 = int(input("Masukkan bilangan 1: "))
    bil2 = int(input("Masukkan bilangan 2: "))
    hasil = bil1 + bil2
    print("Hasilnya:",hasil)
    
def kurang():
    bil1 = int(input("Masukkan bilangan 1: "))
    bil2 = int(input("Masukkan bilangan 2: "))
    hasil = bil1 - bil2
    print("Hasilnya:",hasil)

def bagi():
    bil1 = int(input("Masukkan bilangan 1: "))
    bil2 = int(input("Masukkan bilangan 2: "))
    hasil = bil1/bil2
    print("Hasilnya:",hasil)

def kali():
    bil1 = int(input("Masukkan bilangan 1: "))
    bil2 = int(input("Masukkan bilangan 2: "))
    hasil = bil1 * bil2
    print("Hasilnya:",hasil)

def pangkat():
    bil1 = int(input("Masukkan bilangan 1: "))
    bil2 = int(input("Masukkan bilangan 2: "))
    hasil = bil1**bil2
    print("Hasilnya:",hasil)

calculator()