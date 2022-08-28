'''이거 sort를 알아야 하는데, lambda 알아놓기!!!
2번째좌표로 먼저 정리하고 1번째 좌표로 정리하려면
튜플 이용해서 묶어서 쓰면됨
내림차순 하고 싶으면 - 붙이면됨
-x[1] 이런식으로'''

N = int(input())
arr = []
for i in range(N):
    a = list(map(int, input().split()))
    arr.append(a)
arr.sort(key=lambda x: (x[1], x[0]))

for i in range(len(arr)):
    for j in range(2):
        print(arr[i][j], end=' ')
    print()
