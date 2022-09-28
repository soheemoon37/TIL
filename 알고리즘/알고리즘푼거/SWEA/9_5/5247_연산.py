from collections import deque    # 데크사용위한거1, 데크 안쓰면 시간초과뜸

def bfs(N):
    visited = [0] * 1000001  # 마지막에 1 안 붙이면 인덱스에러남..
    # 연산의 중간 결과도 항상 백만 이하의 자연수~, 시간복잡도 줄이기 위해 maxV 미리 정해놓기
    maxV = 1000000
    q = deque([])                                       # 데크 사용위한거2
    q.append(N)
    visited[N] = 1
    while q:
        N = q.popleft()                                 # 데크사용3

        # +1, -1, *2, -10 하나씩 해볼거임
        if 0 < N+1 <= maxV and visited[N+1] == 0:       # 아직 방문안한곳만 체크
            q.append(N+1)
            visited[N+1] = visited[N] + 1               # 너비우선이니까 그 전꺼에서 더하기 1
            if N+1 == M:                                # M 나오면 바로 출력
                print(visited[N+1]-1)
                break

        if 0 < N-1 <= maxV and visited[N-1] == 0:
            q.append(N-1)
            visited[N-1] = visited[N] + 1
            if N-1 == M:
                print(visited[N-1]-1)
                break

        if 0 < N*2 <= maxV and visited[N*2] == 0:
            q.append(N*2)
            visited[N*2] = visited[N] + 1
            if N*2 == M:
                print(visited[N*2]-1)
                break

        if 0 < N - 10 <= maxV and visited[N-10] == 0:
            q.append(N - 10)
            visited[N - 10] = visited[N] + 1
            if N - 10 == M:
                print(visited[N - 10]-1)
                break


T = int(input())
for _ in range(1, T+1):
    print(f'#{_}', end=' ')
    N, M = map(int, input().split())
    bfs(N)