import sys
input = sys.stdin.readline

N = int(input())
arr = []
arr1 = list(range(1, N+1))

for i in range(N):
    arr.append(int(input()))

arr.sort()

total = 0
for i in range(N):
    total += abs(arr[i] - arr1[i])
print(total)



