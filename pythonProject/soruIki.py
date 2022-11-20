def tamSayiBolenBulma(sayi):
    bolenListesi=[]
    for i in range(1,sayi+1):
        if(sayi%i==0):
            bolenListesi.append(-i)
            bolenListesi.append(i)
            bolenListesi.sort()
    return bolenListesi

sayiGirisi=input("bir sayı giriniz: ")
print(tamSayiBolenBulma(int(sayiGirisi)))