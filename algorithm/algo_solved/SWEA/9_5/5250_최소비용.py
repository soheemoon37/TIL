def bfs(i, j):
    visited = [[1000000] * N for i in range(N)]  # visited 에 큰 수 넣어놓기
    visited[i][j] = 0
    q = []
    q.append((i, j))
    while q:
        ci, cj = q.pop(0)
        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            ni, nj = ci + di, cj + dj
            if ni < 0 or ni >= N or nj < 0 or nj >= N:
                continue
            # 이 부분 처음에 안 해서 틀렸음. 차이가 마이너스일 수도 있는데, 이 때는 그냥 0으로 놔둬야함.
            cha = arr[ni][nj] - arr[ci][cj]
            if cha < 0:
                cha = 0
            if visited[ni][nj] > visited[ci][cj] + 1 + cha:
                visited[ni][nj] = visited[ci][cj] + 1 + cha
                q.append((ni, nj))
    return visited[N-1][N-1]

T = int(input())
for _ in range(1, T+1):
    print(f'#{_}', end=' ')
    N = int(input())
    arr = [list(map(int, input().split())) for i in range(N)]
    print(bfs(0, 0))