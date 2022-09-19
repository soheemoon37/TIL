'''swea d2
1시간 15분 걸림.
일단 방향 설정 해놓고 십자 모양 합 구하고
또 방향 설정해놓고 엑스자방향 합 구하면 됨'''

T = int(input())

for _ in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for i in range(N)]
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    total_list = []
    for i in range(N):
        for j in range(N):
            total = arr[i][j]
            for k in range(4):
                for m in range(1, M):
                    ni = i + di[k] * m
                    nj = j + dj[k] * m
                    if 0 <= ni < N and 0 <= nj < N:
                        total += arr[ni][nj]
            total_list.append(total)

    ddi = [1, -1, -1, 1]
    ddj = [1, -1, 1, -1]
    total_list1 = []
    for i in range(N):
        for j in range(N):
            total1 = arr[i][j]
            for k in range(4):
                for m in range(1, M):
                    ni = i + ddi[k] * m
                    nj = j + ddj[k] * m
                    if 0 <= ni < N and 0 <= nj < N:
                        total1 += arr[ni][nj]
            total_list1.append(total1)

    a = max(total_list)
    b = max(total_list1)
    print(f'#{_} {max(a, b)}')

