

import sys

sys.stdin = open("1219_길찾기.txt")

def dfs(s, e2):
    visited = [0] * 100
    stack = [0] * 100
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




for _ in range(1, 11):
    t, e = map(int, input().split())
    adjList = [[] for _ in range(100)]
    arr = list(map(int, input().split()))
    for i in range(0, 2 * e, 2):
        adjList[arr[i]].append(arr[i+1])
    dfs(0, 99)

