
from collections import deque
import sys

input = sys.stdin.readline

def bfs(x):
    visited = [-1] * (N+1)
    visited[x] = 0
    q = deque([])
    q.append(x)
    while q:
        x = q.popleft()
        for w in adjList[x]:
            if visited[w] == -1:
                q.append(w)
                visited[w] = visited[x] + 1
    check = False
    for i in range(N+1):
        if visited[i] == K:
            print(i)
            check = True
    if check == False:
        print(-1)


N, M, K, X = map(int, input().split())
adjList = [[] for i in range(N+1)]
for i in range(M):
    a, b = map(int, input().split())
    adjList[a].append(b)
bfs(X)
