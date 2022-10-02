# 베이비진
# 0921 연습문제2

def f(i, k, r):
    global ans
    cnt = 0
    if i == r:
        if (p[0] + 2 == p[2] and p[1] + 1 == p[2]) or (p[0] == p[1] and p[1] == p[2]):
            cnt += 1
        if (p[3] + 2 == p[5] and p[4] + 1 == p[5]) or (p[3] == p[4] and p[4] == p[5]):
            cnt += 1
        if cnt == 2:
            ans = True

    else:
        for j in range(k):
            if used[j] == 0:
                used[j] = 1
                p[i] = a[j]
                f(i+1, k, r)
                used[j] = 0

T = int(input())
for _ in range(T):
    N = 6
    R = 6
    a = list(map(int, input()))
    ans = False
    # print(a)
    used = [0] * N
    p = [0] * R
    f(0, N, R)
    print(ans)