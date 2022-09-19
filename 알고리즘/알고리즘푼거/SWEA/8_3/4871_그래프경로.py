import sys

sys.stdin = open("4871_그래프경로.txt")

# 어제 수업 내용 코드 그대로 사용함
# 변수만 몇 개 바꿔줬음
# 인접 리스트 만드는 거 연습하세요

def dfs(s, e2):
    visited = [0] * (v+1)
    stack = [0] * (v+1)
    top = -1
    visited[s] = 1
    while True:
        for w in adjList[s]:
            if visited[w] == 0:
                top += 1
                stack[top] = s
                s = w
                visited[w] = 1
                break
        else:
            if top != -1:
                s = stack[top]
                top -= 1
            else:
                break
    if visited[e2] == 1:
        print(f'#{_} 1')
    else:
        print(f'#{_} 0')



T = int(input())
for _ in range(1, T+1):
    v, e = map(int, input().split())
    adjList = [[] for _ in range(v+1)]
    for c in range(e):
        idx, val = map(int, input().split())
        adjList[idx].append(val)
    s, e2 = map(int, input().split())
    dfs(s, e2)

