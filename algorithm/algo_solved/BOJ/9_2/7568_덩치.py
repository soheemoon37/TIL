# 9/6. 실버5. 브루트포스 알고리즘

N = int(input())
arr = []
for i in range(N):
    a = list(map(int, input().split()))
    arr.append(a)

for i in arr:
    rank = 1
    for j in arr:
        if i[0] < j[0] and i[1] < j[1]:
            rank += 1
    print(rank, end=' ')