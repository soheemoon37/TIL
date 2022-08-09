# 평균은 넘겠지. 8월 9일. 브론즈1

import sys

sys.stdin = open("4344.txt")

T = int(input())

for t in range(T):
    arr = list(map(int, input().split()))
    total = 0
    for i in range(1, len(arr)):
        total += arr[i]
    average = total / arr[0] # 평균 구하기
    average_a = []
    for c in range(1, len(arr)):
        if arr[c] > average:
            average_a.append(arr[c]) # 평균 넘는 값 구하기
    answer1 = (len(average_a) / arr[0]) * 100 # 평균 넘는 값 비율 구하기
    answer2 = format(float(answer1), ".3f") # 소수점 3번째 자리까지 조절
    print(f'{answer2}%')
