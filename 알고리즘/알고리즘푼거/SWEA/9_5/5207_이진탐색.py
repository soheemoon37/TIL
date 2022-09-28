def binary_search(a, N, key):
    global cnt
    start = 0
    end = N - 1
    flag1 = flag2 = 0
    while start <= end:
        center = (start+end) // 2
        if a[center] == key:
            cnt += 1
            return

        elif a[center] > key:
            if flag1 == 1:
                break
            else:
                flag1 += 1
                end = center - 1
            flag2 = 0
        else:
            if flag2 == 1:
                break
            else:
                flag2 += 1
                start = center + 1
            flag1 = 0
    return

T = int(input())
for _ in range(1, T+1):
    print(f'#{_}', end=' ')
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    B = list(map(int, input().split()))
    cnt = 0
    for i in B:
        binary_search(A, N, i)
    print(cnt)
