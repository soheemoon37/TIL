import sys

sys.stdin = open("1979_어디에단어가.txt")

# 이 문제도 힘들었음 ㅠㅠㅠ
# 일단 arr 받고, 세로 방향 리스트도 arr3로 만들기
# 이게 1이 K만큼 연속으로 나오고 양 옆은 0이 있는 게 편하니까, insert랑 append 이용해서 양가에 0을 넣어줌
# 그 다음은 cnt 세야하는데, 범위가 좀 머리아픔
# j는 1부터 N-K+2까지만 검사하면 됨. 그리고 슬라이스 이용해서 K칸만큼 1이고 양옆은 0이면
# cnt 늘리기. 세로도 똑같이 해줌

T = int(input())
for _ in range(1, T+1):
    N, K = map(int, input().split())

    arr = [list(map(int, input().split())) for _ in range(N)]
    arr3 = []
    for i in range(N):
        arr2 = []
        for j in range(N):
            arr2.append(arr[j][i])
        arr3.append(arr2)

    for i in range(N):
        arr[i].insert(0, 0)
        arr[i].append(0)
    for i in range(N):
        arr3[i].insert(0, 0)
        arr3[i].append(0)

    cnt = 0
    for i in range(N):
        for j in range(1, N-K+2):
            if arr[i][j:j+K] == [1] * K and arr[i][j-1] == 0 and arr[i][j+K] == 0:
                cnt += 1
    for i in range(N):
        for j in range(1, N-K+2):
            if arr3[i][j:j+K] == [1] * K and arr3[i][j-1] == 0 and arr3[i][j+K] == 0:
                cnt += 1
    print(f'#{_} {cnt}')



