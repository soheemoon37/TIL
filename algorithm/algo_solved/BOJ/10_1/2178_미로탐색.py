from collections import deque

def bfs(i, j):
    visited = [[10000] * M for i in range(N)]
    visited[0][0] = 1
    q = deque([])
    q.append((i, j))
    while q:
        ci, cj = q.popleft()
        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            ni, nj = ci + di, cj + dj
            if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] == 1:
                if visited[ni][nj] > visited[ci][cj] + 1:
                    visited[ni][nj] = visited[ci][cj] + 1
                    q.append((ni, nj))
    return visited[N-1][M-1]



N, M = map(int, input().split())
arr = [list(map(int, input())) for i in range(N)]
print(bfs(0, 0))
