N, K = map(int, input().split())
list1 = list(range(1, K+1))
list2 = list(range(N, N-K, -1))
total1 = 1
total2 = 1
for i in list1:
    total1 = total1 * i
for i in list2:
    total2 = total2 * i
print(int(total2 / total1) % 10007)
