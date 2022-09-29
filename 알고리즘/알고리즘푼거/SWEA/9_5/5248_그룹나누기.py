def find_set(x):
    while x != rep[x]:
        x = rep[x]
    return x

def union(x, y):
    rep[find_set(y)] = find_set(x)


T = int(input())
for _ in range(1, T+1):
    print(f'#{_}', end=' ')
    N, M = map(int, input().split())
    rep = [i for i in range(N + 1)]
    arr = list(map(int, input().split()))
    for i in range(0, len(arr), 2):
        union(arr[i], arr[i+1])
    cnt = 0
    for i in range(1, N+1):  # 자기자신을 가리키는 수의 개수 찾으면 됨.
        if i == rep[i]:
            cnt += 1
    print(cnt)
