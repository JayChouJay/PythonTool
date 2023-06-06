# 选择排序
def selectionSort(a):
    n = len(a)
    for i in range(n - 1):
        #print(i)
        min = i
        for j in range(i + 1, n):
            if a[j] < a[min]:
                min = j
            a[i], a[min] = a[min], a[i]


# 冒泡排序
def bobbleSort(a):
    n = len(a)
    for i in range(n - 1):
        for j in range(0, n-i-1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]

def bobbleSort2(a):
    n = len(a)
    for i in range(n - 1,-1,-1):
        for j in range(0, i):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]

#插入排序


#选择排序
a = [8, 5, 6, 4, 3, 7, 10, 2]
selectionSort(a)
print(a)

#冒泡排序
a = [8, 5, 6, 4, 3, 7, 10, 2]
bobbleSort(a)
print(a)

a = [8, 5, 6, 4, 3, 7, 10, 2]
bobbleSort2(a)
print(a)

#插入排序