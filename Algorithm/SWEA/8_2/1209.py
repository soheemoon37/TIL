import sys

sys.stdin = open("1209.txt")


for n in range(1, 11):
    test_case = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    maxV1 = 0
    for i in range(100): # 행의 합 중 최대값
        total1 = 0
        for j in range(100):
            total1 += arr[i][j]
        if maxV1 < total1:
            maxV1 = total1
    maxV2 = 0
    for j in range(100): # 열의 합 중 최대값
        total2 = 0
        for i in range(100):
            total2 += arr[i][j]
        if maxV2 < total2:
            maxV2 = total2
    total3 = 0
    for i in range(100): # 오른쪽아래 대각선 합
        total3 += arr[i][i]
    total4 = 0
    for i in range(100): # 왼쪽아래 대각선 합
        total4 += arr[i][99-i]
    maxV = max(maxV1, maxV2, total3, total4)
    print(f'#{test_case} {maxV}')