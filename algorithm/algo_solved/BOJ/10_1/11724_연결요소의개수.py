import sys
input = sys.stdin.readline

# 최종부모고르기
def find_set(x):
    while x != rep[x]:
        x = rep[x]
    return x

# 하나의 집합으로 합치기
def union(x, y):
    rep[find_set(y)] = find_set(x)

V, E = map(int, input().split())    # V 마지막 정점, 0~V번 정점. 개수 (V+1)개
rep = [i for i in range(V+1)]       # 대표원소 배열

for _ in range(E):
    u, v = map(int, input().split())
    union(u, v)

# 대표가 자기자신인 거 개수 세기
cnt = 0
for i in range(len(rep)):
    if rep[i] == i:
        cnt += 1
# 0 인덱스 빼고 출력
print(cnt-1)