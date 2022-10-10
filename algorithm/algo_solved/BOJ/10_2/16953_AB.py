# ㄱㄱㄹ. 평소에 내가 하던 bfs 방식으로는 메모리초과뜸
# 아래 방식이 훨 나은듯.. 공부하기!!

from collections import deque

import sys
input = sys.stdin.readline

def bfs(n, m):
    # cnt 를 리스트에 넣어서 풀기
    q = deque([(n, 1)])

    while q:
        n, cnt = q.popleft()
        if n*2 <= m:  # m 보다 작은 경우에만 살펴보기
            q.append((n*2, cnt+1))
            if n*2 == m:
                return cnt+1
        if n*10+1 <= m:
            q.append((n*10+1, cnt+1))
            if n*10+1 == m:
                return cnt+1
    return -1

n, m = map(int, input().split())
print(bfs(n, m))

# visited 있는 방법으로 했는데 메모리초과 떠서 다른방법찾음
# def bfs(n, m):
#     visited[n-n] = 1
#     q = deque([])
#     q.append(n)
#     while q:
#         a = q.popleft()
#         if a*2 <= m and visited[a*2-n] == 0:
#             visited[a*2-n] = visited[a-n] + 1
#             q.append(a*2)
#             # print(visited)
#             if a*2 == m:
#                 return visited[a*2-n]
#         b = int(str(a) + '1')
#         if b <= m and visited[b-n] == 0:
#             visited[b-n] = visited[a-n] + 1
#             q.append(b)
#             # print(visited)
#             if b == m:
#                 return visited[b-n]
#     return -1

