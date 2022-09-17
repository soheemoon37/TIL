
'''여기서 포인트는 일단 지금 있는 곳에서 갈 수 있는 방향들을 탐색해봄. 그러고 파이프가 있으면
이제 연결되는지 확인하는거임. 지금 있는 곳이 x,y 이면 상하좌우 방향은 nx,ny 이고 여기서 mx, my 를 탐색하는데 x,y 랑 연결이 되면
연결이 되는 곳임'''
def bfs(n, m):
    direction = [(0, -1), (-1, 0), (0, 1), (1, 0)] # 좌0상1우2하3
    pipe = [[], [0, 1, 2, 3], [1, 3], [0, 2], [1, 2], [3, 2], [3, 0], [1, 0]] # 위에 방향에서 갈수 있는 곳의 방향 인덱스를 적기
    while q:
        x, y = q.pop(0)
        sub = pipe[tunnel[x][y]] # pipe 에 있는 번호
        for i in sub:
            di, dj = direction[i]
            nx, ny = x + di, y + dj # 상하좌우 이어지는 인덱스번호
            # 인덱스 값이 범위 안에 있어야 하고 아직 방문하지 않은 곳이어야 하고, 파이프가 있어야함
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == 0 and tunnel[nx][ny] != 0:
                next = pipe[tunnel[nx][ny]] # 위의 조건이 만족하면, next 가 될 수 있음
                for j in next: # 이제 연결되는지 확인해야함. mx, my 구하기
                    ddi, ddj = direction[j]
                    mx, my = nx + ddi, ny + ddj
                    if mx == x and my == y: # 구한 mx,my 가 x,y랑 같다면 연결된거임. 그러면 q 에 추가해서 방향 계속 탐색해야함
                        q.append((nx, ny))
                        visited[nx][ny] = visited[x][y] + 1 # visited 에는 이전값보다 1 높은 값 넣기

T = int(input())
for _ in range(1, T+1):
    print(f"#{_}", end=' ')
    n, m, r, c, l = map(int, input().split())
    tunnel = [list(map(int, input().split())) for i in range(n)]
    visited = [[0] * m for _ in range(n)]
    visited[r][c] = 1
    q = [(r, c)] # q 에 현재 인덱스 번호 튜플로 넣기
    bfs(n, m)

    cnt = 0 # visited 의 값이 l 보다 작거나 같으면 cnt 에 1 추가
    for i in range(n):
        for j in range(m):
            if 0 < visited[i][j] <= l:
                cnt += 1
    print(cnt)
