''' ㄱㄱㄹ. 원래 내가 풀던 식으로 bfs 함수 쓰기보다는 첨부터 1인거 q 에 넣어서 나아가는게 나음
그리고 visited 쓰는거 보다 arr 에서 값 바꾸는게 나음. 다 1인 경우는 어짜피 q 안 돌고 max 값 1 이라서 답 0 나오고
0이 포함된 경우는 골라내서 ans 바꾸면 되고, 나머지 경우는 max 값에서 -1 해서 답 찾으면됨 '''

from collections import deque
import sys

input = sys.stdin.readline

M, N = map(int, input().split())
arr = [list(map(int, input().split())) for i in range(N)]
q = deque([])
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            q.append((i, j))
while q:
    ci, cj = q.popleft()
    for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
        ni, nj = ci + di, cj + dj
        if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] == 0:
            arr[ni][nj] = arr[ci][cj] + 1
            q.append((ni, nj))
# 이거 이중리스트에서 max 값 찾는 거 알아두기!! map 쓰면돼~~
ans = max(map(max, arr)) - 1
for i in arr:  # 이중 리스트에서 특정 값 골라내는 법도 알아두기~~
    if 0 in i:
        ans = -1
print(ans)
