from collections import deque

def bfs(i, j):
    visited = [[100000] * N for i in range(N)]       # 갓도원팁. visited 에 max 값으로 일단 다 채워두기. 후에 최소값으로 계속 변경.
    visited[i][j] = 0                                # 처음 값은 0으로 해야 됨. 자기자신일 때는 0
    q = deque([(i, j)])                              # deque 안쓰면 너무 느려짐..
    q.append((i, j))                                 # 최초값은 넣어놓기
    while q:                                         # q 가 있는 동안 실행
        ci, cj = q.popleft()                         # popleft~~

        for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:           # 4방향 탐색
            ni, nj = ci + di, cj + dj                               # 다음인덱스에서
            if ni < 0 or ni >= N or nj < 0 or nj >= N:              # 인덱스범위지정하기
                continue
            # 여기가 포인트임!!!!! 갱신할 때만 q 에 어펜드해주기
            if visited[ni][nj] > visited[ci][cj] + arr[ni][nj]:     # 최소값비교할거임. 현재값보다 갱신값이 작으면 갱신하기
                visited[ni][nj] = visited[ci][cj] + arr[ni][nj]
                q.append((ni, nj))
    return visited[N-1][N-1]                                        # 마지막 값 출력


T = int(input())
for _ in range(1, T+1):
    print(f'#{_}', end=' ')
    N = int(input())
    arr = [list(map(int, input())) for i in range(N)]
    print(bfs(0, 0))

