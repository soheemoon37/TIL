def SelectionSort(A):
    n = len(A)
    for i in range(0, n-1):
        mini = i
        for j in range(i+1, n):
            if A[j] < A[mini]:
                mini = j
        A[mini], A[i] = A[i], A[mini]
    return A

A = [2, 4, 6, 1, 9, 8, 7, 0]
a = SelectionSort(A)
print(a)