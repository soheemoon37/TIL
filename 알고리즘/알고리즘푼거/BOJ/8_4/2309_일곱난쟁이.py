# 브론즈1. 부분집합으로 구했음

난쟁이 = []

for i in range(9):
    난쟁이.append(int(input()))


n = len(난쟁이)
난쟁이집합 = []
for i in range(1<<n):
    a = []
    for j in range(n):
        if i & (1<<j):
            a.append(난쟁이[j])
    난쟁이집합.append(a)
for i in range(len(난쟁이집합)):
    if len(난쟁이집합[i]) == 7 and sum(난쟁이집합[i]) == 100:
        a = 난쟁이집합[i]
a.sort()
for i in range(len(a)):
    print(a[i])

