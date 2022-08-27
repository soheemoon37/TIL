'''15분걸림. swea d2 문제
이중리스트에서 지점 정해놓고 그 지점이 1이면서
아래쪽도 1이면 카운트에 더함 아니면 브레이크
가로도 똑같이 지정해서 고고'''

T = int(input())
for _ in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for i in range(N)]
    cnt_list = []

    for i in range(N):
        for j in range(M):
            cnt = 0
            for k in range(N):
                if arr[i][j] == 1:
                    if i+k < N and arr[i+k][j] == 1:
                        cnt += 1
                    else:
                        break
            cnt_list.append(cnt)
    for i in range(N):
        for j in range(M):
            cnt = 0
            for k in range(M):
                if arr[i][j] == 1:
                    if j+k < M and arr[i][j+k] == 1:
                        cnt += 1
                    else:
                        break
            cnt_list.append(cnt)
    print(f'#{_} {max(cnt_list)}')
