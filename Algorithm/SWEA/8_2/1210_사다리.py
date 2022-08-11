import sys

sys.stdin = open("1210_사다리.txt")

for test_case in range(1, 11):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    endX = arr[99].index(2)
    i, j = [99, endX]                                             # 도착지점 인덱스 찾아놓기
    while i != 0:                                                 # i가 0이 아닌동안 진행. 그거까지만 해도 j가 나옴.
        if j-1 >= 0 and arr[i][j-1] == 1:                         # 왼쪽 벽을 지정해둠. 그리고 왼쪽에 1이 있을 때
            arr[i][j-1] = 0                                       # 현재 자리를 0으로 바꾸고 j 자리를 왼쪽으로 한 칸 옮김.
            j = j - 1
        elif j+1 <= 99 and arr[i][j+1] == 1:                      # 오른쪽 벽을 정해둠. 그리고 오른쪽에 1이 있을 때
            arr[i][j+1] = 0                                       # 현재 자리를 0으로 바꾸고 j의 자리를 오른쪽으로 한 칸 옮김.
            j = j + 1
        else:                                                     # 그렇지 않은 경우는 현재 자리를 0으로 바꾸고 계속 위로 올라감.
            arr[i-1][j] = 0
            i = i - 1
    print(f'#{test_case} {j}')






