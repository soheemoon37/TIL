def bfs(v, N):  # v 시작정점, N 마지막 정점
    visited = [0] * (N+1)  # visited 생성
    q = []
    q.append(v)
    visited[v] = 1
    while q:
        v = q.pop(0)
        print(v)
        for w in adjList[v]:
            if visited[w] == 0:
                q.append(w)
                visited[w] = visited[v] + 1

a, b = map(int, input().split())
adjList = [[] for _ in range(a+1)]
arr = list(map(int, input().split()))
for i in range(0, 2 * b, 2):
    adjList[arr[i]].append(arr[i + 1])
    adjList[arr[i+1]].append(arr[i])
bfs(1, 7)