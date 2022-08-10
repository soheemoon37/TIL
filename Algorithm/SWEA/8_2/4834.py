# 숫자카드

import sys

sys.stdin = open("4834.txt")

test_case = int(input())

for t in range(1, test_case+1):
    N = int(input())
    arr = list(map(int, input()))
    cnt = [0] * 10                      # 카운팅 정렬 사용
    for i in range(N):
        cnt[arr[i]] += 1
    max_idx = 0
    maxV = 0
    for c in range(len(cnt)):           # cnt에서 최대값과 그 인덱스 구하기.
        if cnt[c] >= maxV:
            max_idx = c
            maxV = cnt[c]
    print(f'#{t} {max_idx} {maxV}')     # 근데 정답은 뒤바뀌어야됨.