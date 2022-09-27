
def f(i, k, total):
    global rst
    if total >= rst:
        return
    if i == k:
        rst = total
    else:
        for j in range(k):
            if used[j] == 0:
                used[j] = 1
                p[i] = arr[i][j]
                f(i+1, k, total+arr[i][j])
                used[j] = 0

T = int(input())
for _ in range(1, T+1):
    print(f'#{_}', end=' ')
    N = int(input())
    arr = [list(map(int, input().split())) for i in range(N)]
    a = [i for i in range(N)]
    used = [0] * N
    p = [0] * N
    rst = 15 * 99
    f(0, N, 0)
    print(rst)