import random

#############Bubble Sort (пузырьковая сортировка)#############

a = [15,5,6,43,12,8,34,1]
for i in range(0,len(a)-1):
    for j in range(0,len(a)-1-i):
        if a[j]>a[j+1]:
            a[j],a[j+1]=a[j+1],a[j]
print(a)

#############Selection Sort (сортировка выбором)#############

b = [15,5,6,43,12,8,34,1]
for i in range(len(b)):
    minimum = i
    for j in range(i+1,len(b)):
        if b[j] < b[minimum]:
            minimum = j
    b[minimum],b[i] = b[i],b[minimum]
print(b)

#############Insertion Sort (сортировка вставками)#############

c = [15,5,6,43,12,8,34,1]
for i in range (len(c)):
    cursor = c[i]
    pos = i   
    while pos > 0 and c[pos - 1] > cursor:
        c[pos] = c[pos - 1]
        pos = pos - 1
    c[pos] = cursor
print(c)


#############Merge Sort (сортировка слиянием)#############
def QuickSort(A, l, r):
    if l >= r:
        return 
    else:
        q = random.choice(A[l:r + 1])
        i = l
        j = r
        while i <= j:
            while A[i] < q:
                i += 1
            while A[j] > q:
                j -= 1
            if i <= j: 
                A[i], A[j] = A[j], A[i]
                i += 1
                j -= 1 
                QuickSort(A, l, j)
                QuickSort(A, i, r)