
from collections import Counter # 최빈값구하기
import sys
input = sys.stdin.readline


N = int(input())
arr = [int(input()) for i in range(N)]
arr.sort()
n = sum(arr) / N

print(round(n)) # 산술평균
print(arr[N//2]) # 중앙값

# 최빈값 구하기
cnt = Counter(arr)
a = cnt.most_common()
b = list()
b.append(a[0])

for i in range(1, len(a)):
    if a[i][1] == a[0][1]:
        b.append(a[i])

if len(b) == 1:
    print(b[0][0])
else:
    print(b[1][0])

print(max(arr)-min(arr)) # 범위