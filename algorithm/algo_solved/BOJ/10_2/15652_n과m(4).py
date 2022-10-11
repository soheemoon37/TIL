# 순열 2번째 방법
# pypy로 통과됨. python 은 시간초과뜸

import sys
input = sys.stdin.readline

def f(n, r, i):
    if i == r:
        for i in range(len(p)-1):
            if p[i] <= p[i+1]:
                continue
            else:
                return
        else:
            print(*p)
    else:
        for j in range(n):
            if used[j] == 0:
                p[i] = a[j]
                f(n, r, i+1)

N, R = map(int, input().split())
a = [i for i in range(1, N+1)]
used = [0] * N
p = [0] * R
f(N, R, 0)