'''너비 우선 탐색이라 bfs 써야함. 딕셔너리로 해보려했는데 어려움'''

def bfs(v):
    visited = [0] * 101
    queue = [v]
    visited[v] = 1
    while queue:
        t = queue.pop(0)
        for a in adjlist[t]:
            if not visited[a]:               # 방문한적 있으면 신경안쓰기 위해
                queue.append(a)
                visited[a] = visited[t] + 1  # 레벨이 같아야 해서 그 전꺼에서 1더함
    idx = []
    for i in range(len(visited)):            # 제일 높은 레벨에서 가장 큰 인덱스값 구하기
        if visited[i] == max(visited):
            idx.append(i)
    return max(idx)

for _ in range(1, 11):
    print(f'#{_}', end=' ')
    N, start = map(int, input().split())
    arr = list(map(int, input().split()))
    adjlist = [[] for _ in range(101)]
    for i in range(0, N, 2):          # adjlist 만들기
        if arr[i+1] not in adjlist[arr[i]]:
            adjlist[arr[i]].append(arr[i+1])
    print(bfs(start))
