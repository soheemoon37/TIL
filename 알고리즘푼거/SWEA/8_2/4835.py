# 구간합

import sys

sys.stdin = open("4835.txt")

test_case = int(input())


for t in range(1, test_case+1):
    total_a = []
    N, M = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    for n in range(N-M+1):                       # 계산해보니 N-M+1까지만 보면됨.
        total = 0
        for m in range(n, n+M):
            total += arr[m]                      # total값 구하는데 n이랑 M 이용해서 범위 정해야됨.
        total_a.append(total)
    a = max(total_a) - min(total_a)              # 차이 구하기
    print(f'#{t} {a}')


