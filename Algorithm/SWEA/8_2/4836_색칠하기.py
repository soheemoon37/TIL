import sys

sys.stdin = open("4836_색칠하기.txt")

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    arr = [[0] * 10 for _ in range(10)]    # 0으로 이중리스트 만들어놓기
    for _ in range(N):    # 입력값에서 색칠할 부분에 1 더하기
        r1, c1, r2, c2, color = list(map(int, input().split()))
        for i in range(r1, r2 + 1):
            for j in range(c1, c2 + 1):
                arr[i][j] += 1
    count = 0    # 색칠한 부분이 2이상이면 겹쳐있는 부분이니까 그 부분을 세기
    for i in range(10):
        for j in range(10):
            if arr[i][j] >= 2:
                count += 1

    print(f'#{test_case} {count}')
