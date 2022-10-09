'''bfs 함수를 2개로 나눴음'''

from collections import deque

def bfs(i, j):
    visited[i][j] = 1
    q = deque([])
    q.append((i, j))
    while q:
        ci, cj = q.popleft()
        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            ni , nj = ci + di, cj + dj
            if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] == 0 and arr[ci][cj] == arr[ni][nj]:  # 색깔 같을 때만 방문
                visited[ni][nj] = visited[ci][cj] + 1
                q.append((ni, nj))

def bfs1(i, j):
    visited[i][j] = 1
    q = deque([])
    q.append((i, j))
    while q:
        ci, cj = q.popleft()
        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            ni , nj = ci + di, cj + dj
            if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] == 0 and arr[ni][nj] != 'B':  # R 이랑 G 랑 같은걸로보니깐 B 아닐 때 방문
                visited[ni][nj] = visited[ci][cj] + 1
                q.append((ni, nj))

    

N = int(input())
arr = [list(input()) for i in range(N)]
visited = [[0] * N for i in range(N)]

# 2가지로 나눠서 생각. 색 다 다를 때랑 적록색약인 게 봤을 때
cnt = 0
for i in range(N):
    for j in range(N):
        if visited[i][j] == 0:
            bfs(i, j)
            cnt += 1
print(cnt, end=' ')

visited = [[0] * N for i in range(N)]
cnt1 = 0
for i in range(N):
    for j in range(N):
        # R 이랑 G 일 때는 bfs1 으로 적용
        if arr[i][j] == 'R' and visited[i][j] == 0:
            bfs1(i, j)
            cnt1 += 1
        if arr[i][j] == 'G' and visited[i][j] == 0:
            bfs1(i, j)
            cnt1 += 1
        if arr[i][j] == 'B' and visited[i][j] == 0:
            bfs(i, j)
            cnt1 += 1
print(cnt1)