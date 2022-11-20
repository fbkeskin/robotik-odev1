# (x,y) şeklinde verilen bir üçgende sonradan girilen (x,y)
# ikililerinin alanın içinde olup olmadığını kontrol eden program

# koordinatları verilen üçgenin alanı matris çarpımından gelir.
# (x1,y1),(x2,y2),(x3,y3)
# alan= [x1(y2-y3)+x2(y3-y1)+x3(y1-y2)]/2
def alan(x1, y1, x2, y2, x3, y3):
    return abs((x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2.0)


# girilen koordinat üçgen alanının içinde mi? kontrolünü yapan function
def icindeMi(x1, y1, x2, y2, x3, y3, x, y):
    A = alan(x1, y1, x2, y2, x3, y3)
    A1 = alan(x, y, x2, y2, x3, y3)
    A2 = alan(x1, y1, x, y, x3, y3)
    A3 = alan(x1, y1, x2, y2, x, y)

    if (A == A1 + A2 + A3):
        return True
    else:
        return False


x1 = input("x1: ")
y1 = input("y1: ")

x2 = input("x2: ")
y2 = input("y2: ")

x3 = input("x3: ")
y3 = input("y3: ")

#print("Girilen koordinatlar: ", x1, y1, x2, y2, x3, y3)

print("bir koordinat girin:")
x = input("x: ")
y = input("y: ")

if (icindeMi(int(x1), int(y1), int(x2), int(y2), int(x3), int(y3), int(x), int(y))):
    print("girilen nokta üçgenin içindedir.")

else:
    print("girilen nokta üçgenin içinde değildir.")
