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
            if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == 1 and visited[ni][nj] == 0:
                visited[ni][nj] = 1
                q.append((ni, nj))
                cnt += 1
    return cnt

N = int(input())
arr = [list(map(int, input())) for i in range(N)]
visited = [[0] * N for i in range(N)]
cnt1 = 0
cnt2 = []
for i in range(N):
    for j in range(N):
        # arr 가 1인데 방문안한곳이면 카운트해주고 bfs 해서 cnt2 에 넣기
        if arr[i][j] == 1 and visited[i][j] == 0:
            cnt1 += 1
            cnt2.append(bfs(i, j))
cnt2.sort()  # 오름차순으로 출력하라했음
print(cnt1)
for i in cnt2:
    print(i)

