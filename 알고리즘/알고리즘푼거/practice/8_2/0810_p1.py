import sys

sys.stdin = open("0810_p1.txt")

T = int(input())

for test_case in range(T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]          # 이중리스트 만들기
    di = [0, 1, 0, -1]                                                 # arr[i][j]에서 오른쪽에서 시계방향으로 인덱스방향 정하기
    dj = [1, 0, -1, 0]
    total = 0
    for i in range(N):                                                 # arr[i][j]를 중심으로 이웃한 인덱스 구하기
        for j in range(N):
            for k in range(4):
                ni = i + di[k]
                nj = j + dj[k]
                if 0 <= ni < N and 0 <= nj < N:                        # 이웃한 인덱스 값이 리스트 범위 안에 있다면
                    total += abs(arr[i][j] - arr[ni][nj])              # 이웃한 값과의 절대값구해서 더하기
    print(f'#{test_case} {total}')


# di = [0, 1, 0, -1]
# dj = [1, 0, -1, 0]
#
# N = 2
# M = 4
#
# arr = [[1, 2, 3, 4], [4, 5, 6, 8]]
#
# for i in range(N):
#     for j in range(M):
#         for k in range(4):
#             ni = i + di[k]
#             nj = j + dj[k]
#             if 0 <= ni < N and 0 <= nj < M:
#                 print(arr[ni][nj])