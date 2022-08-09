# 8월 8일 연습문제1

import sys

sys.stdin = open("gravity.txt")

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        if arr[i] == 0: # 값이 0이면 낙차의 의미가 없으니 continue하기
            continue
        if ans > N-1-i: # 최대값이 i번째가 최대로 떨어질 수 있는 낙차값보다 크면 더 이상 계산 불필요
            break
        count = 0
        for c in range(i+1, len(arr)): # i번째와 그 뒤의 값들을 비교
            if arr[i] <= arr[c]: # i번째보다 더 큰 값이 있다면 count 올리기
                count += 1
        ans = max(ans, N-1-i-count) # 전체에서 본인자리만큼 빼고 뒤에 본인보다 더 큰 값의 개수를 빼면 낙차값 나옴
    print(f'#{test_case} {ans}')




