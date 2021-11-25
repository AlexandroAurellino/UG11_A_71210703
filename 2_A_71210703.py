def ambil_tengah(kalimat,index = 0):
    panjang_kalimat = len(kalimat)
    if panjang_kalimat%2 == 0:
        index_tengah = (panjang_kalimat / 2)
    else:
        index_tengah =  panjang_kalimat//2
    return kalimat[int(index_tengah)+index]

print(ambil_tengah("abcdefg",1))
print(ambil_tengah("abcdefg",2))
print(ambil_tengah("abcd"))