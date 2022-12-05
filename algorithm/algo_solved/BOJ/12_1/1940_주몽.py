# 두 포인터로 하는 문제인데, 나는 하나하나 봐서 파이썬으로는 시간초과남
# 파이파이는 통과됨

n = int(input())
m = int(input())
list1 = list(map(int, input().split()))

total = 0
number = 0
for i in range(n-1):
    total = list1[i]
    while i <= n-2:
        i += 1
        total += list1[i]
        if total == m:
            number += 1
            break
        else:
            total -= list1[i]
print(number)


