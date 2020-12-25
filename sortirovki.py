from random import randint

a = []
for i in range(15):
    a.append(randint(0, 15))


print("1) Сортировка пузырьком")
print("2) Сортировка вставками")
print("3) Сортировка Шелла")
print("4) Быстрая сортировка")
print("Выберите вид сортировки:")
vid = input()
print("Изначальный вид списка - ", a)


def bubblesort(a):
    l = len(a)
    for i in range(l-1):
        for j in range(l-i-1):
            if(a[j] > a[j + 1]):
                a[j], a[j+1] = a[j+1], a[j]
    return print("Отсортированный список - ", a)

def insertionsort(a):
    for i in range(1, len(a)):
        j = i
        while j != 0 and a[j] < a[j - 1]:
            a[j], a[j-1] = a[j-1], a[j]
            j -= 1
    return print("Отсортированный список - ", a)

def shellsort(a):
    l = len(a)
    gap = int(l/2)
    while gap > 0:
        for i in range(gap, l):
            v = a[i]
            j = i
            while j >= gap and a[j-gap] > v:
              a[j] = a[j-gap]
              j -= gap
            a[j] = v
        gap //= 2
    return print("Отсортированный список - ", a)

def quicksort(a):
    l = len(a)
    pivot = l//2
    less, equal, greater = [], [], []
    for i in range(l):
        if a[i] < a[pivot]:
          less.append(a[i])
        elif a[i] > a[pivot]:
          greater.append(a[i])
        else:
          equal.append(a[i])
    if len(less) > 1:
        quicksort(less)
    if len(greater) > 1:
        quicksort(greater)
    return print("Отсортированный список - ", less + equal + greater)


if vid == '1':
    bubblesort(a)
elif vid == '2':
    insertionsort(a)
elif vid == '3':
    shellsort(a)
elif vid == '4':
    quicksort(a)
