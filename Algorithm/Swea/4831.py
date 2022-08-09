# 전기버스

import sys

sys.stdin = open("4831.txt")

test_case = int(input())

for t in range(1, test_case+1):
    K, N, M = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    cnt = [0] * (N + 1)

    for i in range(M): # 충전기 있는 정류장에 1 적기.
        cnt[arr[i]] += 1

    current = 0
    next = 0
    count = 0
    while True:
        # 3번 단계.
        # next 위치가 이제는 current 위치가 되니 대입하기
        # current 에서 K를 더했을 때 N보다 더 가거나 N에 멈추면 이제 그만하기.
        # 아니면 다시 for문이 돔.
        current = next
        if current + K >= N:
            print(f'#{t} {count}')
            break
        # 1번 단계. 현재 위치에서 K 더한 위치부터 내림차순으로 충전기 있는 곳 살펴보기
        # 충전기가 있으면 +K 위치에서 가장 가까운 곳을 next 위치로 두고 count +1하고 빠져나오기.
        for k in range(current + K, current, -1):
            if cnt[k]:
                next = k
                count += 1
                break
        # 2번 단계.
        # 근데 문제는 k에서 아무데도 충전기가 없으면, 0을 출력하도록 해놓기.
        if current == next:
            print(f'#{t} 0')
            break





