import sys

sys.stdin = open("2001_파리퇴치.txt")

# 아 이거 혼자 2시간 헤맸는데, 승태 도움으로 바로품
# 이거 일단 4중 포문이고, total 위치랑 어펜드 위치를 잘 생각해야함
# max 구하려고 total_list 따로 만들어서 max 구했음
# if문 조건 들어가야 되는거도 잊지 말기
# total 이런거 위치 어디에 들어가야 되는지 항상 잘 생각하기

T = int(input())
for _ in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    total_list = []
    for i in range(N):
        for j in range(N):
            total = 0
            for a in range(M):
                for b in range(M):
                    if i+a < N and j+b < N:
                        a2 = arr[i+a][j+b]
                        total += a2
            total_list.append(total)
    print(f'#{_} {max(total_list)}')





