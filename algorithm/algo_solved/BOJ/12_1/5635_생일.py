# 이거보다 더 쉽게 푸는 방법도 있겠지?? 이거는 너무 하나하나 다 구했음

n = int(input())

list1 = []
for i in range(n):
    list2 = list(input().split())
    list1.append(list2)

maxY = 0
for i in range(n):
    if int(list1[i][3]) > maxY:
        maxY = int(list1[i][3])
maxM = 0
for i in range(n):
    if int(list1[i][3]) == maxY:
        if int(list1[i][2]) > maxM:
            maxM = int(list1[i][2])
maxD = 0
for i in range(n):
    if int(list1[i][3]) == maxY:
        if int(list1[i][2]) == maxM:
            if int(list1[i][1]) > maxD:
                maxD = int(list1[i][1])
for i in range(n):
    if int(list1[i][3]) == maxY:
        if int(list1[i][2]) == maxM:
            if int(list1[i][1]) == maxD:
                print(list1[i][0], end=' ')

minY = 2011
for i in range(n):
    if int(list1[i][3]) < minY:
        minY = int(list1[i][3])
minM = 13
for i in range(n):
    if int(list1[i][3]) == minY:
        if int(list1[i][2]) < minM:
            minM = int(list1[i][2])
minD = 32
for i in range(n):
    if int(list1[i][3]) == minY:
        if int(list1[i][2]) == minM:
            if int(list1[i][1]) < minD:
                minD = int(list1[i][1])
for i in range(n):
    if int(list1[i][3]) == minY:
        if int(list1[i][2]) == minM:
            if int(list1[i][1]) == minD:
                print(list1[i][0])