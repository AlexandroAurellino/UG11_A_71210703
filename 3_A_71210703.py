kalimat = input("Masukkan Kalimat : ")
start = int(input("Index Start : "))
stop = int(input("Index Stop : "))

def hitung_hapus(kalimat,start,stop):
    panjang_kalimat = len(kalimat)
    if start > panjang_kalimat:
        hasil = 0.0
    else:
        x = len(kalimat[:start])
        y = len(kalimat[stop+1:])
        sisa = x + y
        z = sisa/panjang_kalimat*100
        hasil = 100 - z

    return hasil

print(hitung_hapus(kalimat,start,stop))