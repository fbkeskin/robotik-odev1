#sıralama algoritmaların kodları

#1-Selection Sort
# dizideki en küçük elemanı bul ve sıraya ekle.
def selectionSort(arr,size):
    for i in range(size):
        min_index=i
        for j in range(i+1,size):
            if arr[j]<arr[min_index]:
                min_index=j

        (arr[i],arr[min_index])=(arr[min_index],arr[i])

dizi = []
n = int(input("Dizi eleman sayısını gir: "))
for i in range(n):
    eleman = int(input())
    dizi.append(eleman)

print(dizi)
selectionSort(dizi,n)
print("sıralanmış dizi:")
print(dizi)


#2-Bubble Sort
#art arda bulunan iki elemanı karşılaştırır ve swap uygular.
def bubbleSort(arr):
    elemanSayisi = len(arr)

    for i in range(elemanSayisi):
        for j in range(0,elemanSayisi-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]

dizi = []
n = int(input("Dizi eleman sayısını gir: "))
for i in range(n):
    eleman= int(input())
    dizi.append(eleman)

print(dizi)
yeniDizi = bubbleSort(dizi)
print("sıralanmış dizi:")
for i in range(n):
    print(dizi[i], end=" ")


#3-Insertion Sort
#sıralanmamış elemanlar, sıralanmış bölümde doğru konuma yerleştirilir.

def insertionSort(arr):
    for i in range(1,len(arr)):
        a=arr[i]
        j=i-1

        while j>=0 and a< arr[j]:
            arr[j+1]=arr[j]
            j = j-1

        arr[j+1]=a
    return arr

dizi = []
n = int(input("Dizi eleman sayısını gir: "))
for i in range(n):
    eleman= int(input())
    dizi.append(eleman)
print(dizi)
print("sıralanmış dizi:")
print(insertionSort(dizi))

#4-Merge Sort
#böl ve yönet mantığı. diziyi 2 ye böler, sıralar ve sonrasında 2 liyi birleştir.



#5-Quick Sort
#divide and conquer algoritması. pivot olarak bir eleman seç ve dizi
#pivot etrafında bölümlere ayrılır.






