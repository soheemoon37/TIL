from collections import deque

def bfs(x, y):
    visited[x][y] = 1
    q = deque([])
    q.append((x, y))
    cnt = 1  # 맨처음값 카운트해주기
    while q:
        ci, cj = q.popleft()
        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            ni, nj = ci + di, cj + dj
            # 인덱스범위안에 있고, arr 이 1이고, 아직 방문안했으면 방문표시해주고 q에 넣고 카운트해주기
            if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] == 1 and visited[ni][nj] == 0:
                visited[ni][nj] = 1
                q.append((ni, nj))
                cnt += 1
    return cnt


T = int(input())
for i in range(T):
    # 인덱스 오류 계속 났었음... N 이 세로고, M 이 가로임.
    M, N, E = map(int, input().split())
    arr = [[0] * M for i in range(N)]  # N 이랑 M 위치 잘보기
    for i in range(E):
        a, b = map(int, input().split())
        arr[b][a] = 1  # 위치도 바꿔놔서 a, b 바꿔야함
    visited = [[0] * M for i in range(N)]  # N 이랑 M 위치 잘보기.

    cnt1 = 0
    for i in range(N):
        for j in range(M):
            # arr 가 1인데 방문안한곳이면 카운트해주고 bfs 해서 cnt2 에 넣기
            if arr[i][j] == 1 and visited[i][j] == 0:
                bfs(i, j)
                cnt1 += 1
    print(cnt1)