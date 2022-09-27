def perm(i, k, r):
    if i == r:
        for i in p:
            print(i, end=' ')
        print()
    else:
        for j in range(k):
            if used[j] == 0:
                used[j] = 1
                p[i] = a[j]
                perm(i+1, k, r)
                used[j] = 0



N, R = map(int, input().split())
a = list(range(1, N+1))
used = [0] * N
p = [0] * R
perm(0, N, R)