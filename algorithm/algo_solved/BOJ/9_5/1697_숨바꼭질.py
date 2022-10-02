from collections import deque

def bfs(N):
    visited = [0] * 100001
    visited[N] = 1
    q = deque([])
    q.append(N)
    while q:
        N = q.popleft()
        if 0 <= N-1 <= 100000 and visited[N-1] == 0:
            q.append(N-1)
            visited[N-1] = visited[N] + 1
            if N-1 == M:
                break
        if 0 <= N+1 <= 100000 and visited[N+1] == 0:
            q.append(N+1)
            visited[N+1] = visited[N] + 1
            if N-1 == M:
                break
        if 0 <= N*2 <= 100000 and visited[N*2] == 0:
            q.append(N*2)
            visited[N*2] = visited[N] + 1
            if N-1 == M:
                break
    return visited[M] - 1
        

N, M = map(int, input().split())
print(bfs(N))