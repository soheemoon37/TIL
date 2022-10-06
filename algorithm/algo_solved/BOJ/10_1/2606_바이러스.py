from collections import deque


def bfs(n):
    visited = [0] * (N+1)
    visited[0] = 1
    visited[1] = 1
    q = deque([])
    q.append(1)
    while q:
        v = q.popleft()
        for w in adjLIST[v]:
            if visited[w] == 0:
                visited[w] = visited[v] + 1
                q.append(w)
    return visited


N = int(input())
E = int(input())
adjLIST = [[] for i in range(N+1)]
for i in range(E):
    a, b = map(int, input().split())
    adjLIST[a].append(b)
    adjLIST[b].append(a)
a = bfs(1)

cnt = 0
for i in range(len(a)):
    if a[i] != 0:
        cnt += 1
print(cnt-2)

