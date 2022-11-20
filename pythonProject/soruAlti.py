#faktoriyel hesabı yapan function
#func. recursive işlem yapmalıdır.

def faktoriyel(sayi):
    if sayi == 0:
        return 1
    else:
        return sayi*faktoriyel(sayi-1)

sayi = int(input("faktoriyel almak istediğiniz sayı: "))
print("sonuc: ",faktoriyel(sayi))