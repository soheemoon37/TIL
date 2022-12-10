# 이중리스트, 1만 나타내서 더하면됨

n = int(input())
list1 = [[0]*101 for i in range(101)]

for i in range(n):
    a, b = map(int, input().split())
    for i in range(10):
        for j in range(10):
            list1[a+i][b+j] = 1
total = 0
for a in list1:
    total += a.count(1)

print(total)