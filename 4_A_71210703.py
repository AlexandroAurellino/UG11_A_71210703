def ambildanbalik(kalimat,start,stop,x):
    a = kalimat[(start-1):(stop)]
    if x == True:
        strlength = len(a)
        flip = a[strlength::-1]
        return flip
    
    else:
        return a

print(ambildanbalik("abcdefg",2,4,True))
print(ambildanbalik("abcdefg",1,5,False))
print(ambildanbalik("Qwerty",3,4,True))
print(ambildanbalik("Qwerty",2,2,False))