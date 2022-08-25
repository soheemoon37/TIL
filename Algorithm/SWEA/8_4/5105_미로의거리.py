# 전형적인 bfs 문제임
# 미로라서 2차원 리스트 써야함
# 상하좌우 비교. visited 값에는 앞에거에서 1씩 더 더해주기
# 저기 return 값을 뭘 해야하나 했는데 visited[i][j] 였음

def bfs(i, j, N):
    visited = [[0] * N for _ in range(N)]
    q = []
    q.append((i, j))
    visited[i][j] = 1
    while q:
        i, j = q.pop(0)
        if arr[i][j] == 3:
            return visited[i][j]
        else:
            for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
                ni, nj = i + di, j + dj
                if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] != 1 and visited[ni][nj] == 0:
                    visited[ni][nj] = visited[i][j] + 1
                    q.append((ni, nj))
    return 2

T = int(input())
for _ in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                a, b = i, j

    print(f'#{_} {bfs(a, b, N)-2}')
