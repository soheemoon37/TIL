# min max

import sys

sys.stdin = open("4828.txt")

test_case = int(input())
# 각각 최대값, 최소값 구하기
for i in range(1, test_case+1):
    N = int(input())
    arr = list(map(int, input().split()))
    maxV = arr[0]
    minV = arr[0]
    for c in range(1, N): # 2개가 다른 내용이라서 똑같이 if라고 써도 무방함.
        if arr[c] > maxV:
            maxV = arr[c]
        if arr[c] < minV:
            minV = arr[c]
    print(f'#{i} {maxV-minV}')