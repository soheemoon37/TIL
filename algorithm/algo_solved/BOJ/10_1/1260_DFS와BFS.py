def dfs(s):
    visited = [0] * (N+1)
    sta = [0] * (N+1)
    top = -1
    visited[s] = 1
    print(s, end=' ')
    while True:
        for w in adjList[s]:
            if visited[w] == 0:
                top += 1
                sta[top] = s
                s = w
                visited[w] = 1
                print(w, end=' ')
                break
        else:
            if top != -1:
                s = sta[top]
                top -= 1
            else:
                break

def bfs(s):
    visited = [0] * (N+1)
    visited[s] = 1
    q = []
    q.append(s)
    while q:
        v = q.pop(0)
        print(v, end=' ')
        for w in adjList[v]:
            if visited[w] == 0:
                q.append(w)
                visited[w] = visited[v] + 1

N, E, V = map(int, input().split())
adjList = [[] for i in range(N+1)]
for i in range(E):
    a, b = map(int, input().split())
    adjList[a].append(b)
    adjList[b].append(a)
for i in range(len(adjList)):
    adjList[i].sort()
dfs(V)
print()
bfs(V)