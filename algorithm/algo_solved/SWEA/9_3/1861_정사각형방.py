# 우하좌상 방향 설정
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def search(start):
    global N
    cnt = 0
    stack = [start] # 여기서 start 튜플임
    while stack:
        x, y = stack.pop() # pop 하고 cnt 에 1 더함
        cnt += 1
        for k in range(4): # 네 방향 탐색
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < N and 0 <= ny < N: # 인덱스가 범위 안에 있을때
                if arr[nx][ny] == arr[x][y] + 1: # 탐색한 인덱스 값이 1이 더 클때
                    stack.append((nx, ny)) # stack 에 추가
    return cnt


T = int(input())
for _ in range(1, T+1):
    print(f"#{_}", end=' ')
    N = int(input())
    arr = [list(map(int, input().split())) for i in range(N)]
    ans = [0, 0]
    for i in range(N):
        for j in range(N):
            cnt = search((i, j)) # 각 자리를 탐색해봄. 그러고 cnt 를 비교하는거임
            if cnt > ans[1]: # 위에 ans 에다가 조건에 맞게 답 바꾸기
                ans[1] = cnt
                ans[0] = arr[i][j]
            elif cnt == ans[1]: # cnt 가 같을 때는
                if arr[i][j] < ans[0]: # 숫자가 더 작아야됨
                    ans[0] = arr[i][j]
    print(f'{ans[0]} {ans[1]}')