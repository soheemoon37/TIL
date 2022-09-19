import sys

sys.stdin = open("1952_수영장.txt")

# 이거 DP 문제이고, 어려움... 3시간 30분에 걸쳐서 푼듯? 승태도움으로 풀었음
# 내가 원래 생각한 대로 구현했으면 평생 못풀었을 듯
# 먼저, 작은 단위부터 비교해 나가서 지워나가면서 큰거끼리 비교하는 아이디어를 써야함
# date를 cost로 바꿀거임. 1일 이용권보다 1달 이용권이 더 싸면 1일 이용권 비용은 의미가 없으니
# 1달 이용권 비용으로 다 바꿈
# 그 다음에 3달께 문제인데, 최대값 인덱스를 찾고, 3달 비용보다 많으면 3달 비용을 price에 추가하고
# 나머지는 0으로 다 바꿔주기
# 이거를 while 문을 써서, else일 때 break 해주면됨
# 그러고 답을 구해보면 2케이스에서 문제가 생김
# 첫번째는 1년 이용권이랑 비교를 안 해서 그런거라 1년 이용권이랑 비교하는 거를 마지막에 넣어주고
# 8번째 케이스에서 또 문제가 생기는데, 이거도 3달치를 max로 구해서 슬라이스를 한 게 문제인거라
# 슬라이스 4번 했을 때, 비용이 더 적은거임
# 이거도 마지막에 조건 대입해주기
# 찝찝하지만 pass는 됨

T = int(input())
for _ in range(1, T+1):
    cost1 = list(map(int, input().split()))
    date1_price = list(map(int, input().split()))
    for i in range(12):
        date1_price[i] = date1_price[i] * cost1[0]
    for i in range(12):
        if date1_price[i] > cost1[1]:
            date1_price[i] = cost1[1]

    price = []
    while True:
        max_idx = 0
        for i in range(10):
            if date1_price[i] + date1_price[i+1] + date1_price[i+2] > date1_price[max_idx] + date1_price[max_idx+1] + date1_price[max_idx+2]:
                max_idx = i

        if date1_price[max_idx] + date1_price[max_idx+1] + date1_price[max_idx+2] > cost1[2]:
            price.append(cost1[2])
            date1_price[max_idx] = 0
            date1_price[max_idx + 1] = 0
            date1_price[max_idx + 2] = 0
        else:
            break

    if cost1[3] < sum(date1_price) + sum(price):
        print(f'#{_} {cost1[3]}')
    elif cost1[2] * 4 < sum(date1_price) + sum(price):
        print(f'#{_} {cost1[2] * 4}')
    else:
        print(f'#{_} {sum(date1_price) + sum(price)}')


