# d2, 달팽이문제
T = int(input())
# 우하좌상 방향 먼저 정해놓기
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
for _ in range(1, T+1):
    print(f'#{_}')
    N = int(input())
    list1 = [[0] * N for i in range(N)]
    x, y = 0, 0
    # 방향 인덱스값 정해놓기
    direction = 0
    # 총 적을 숫자만큼 for문 돌리기
    for n in range(1, N*N + 1):
        list1[x][y] = n
        x += di[direction]
        y += dj[direction]
        # 인덱스 에러 및 다음 칸이 0이 아닌 경우에 if문 쓰기, 다음칸이 0일 아닌경우를 먼저 쓰면 안됨. 에러남.
        if 0 > x or x >= N or 0 > y or y >= N or list1[x][y] != 0:
            # 되돌리기
            x -= di[direction]
            y -= dj[direction]
            # 방향 바꾸기, direction이 4 이상인 경우가 나오면 안돼서 나머지값 쓰기
            direction = (direction + 1) % 4
            # 방향 바꿔서 더해주기
            x += di[direction]
            y += dj[direction]
    # 별 찍으면 바로 나옴        
    for i in list1:
        print(*i)

  