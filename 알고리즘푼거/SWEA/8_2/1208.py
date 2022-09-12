# flatten

import sys

sys.stdin = open("1208.txt")

for i in range(1, 11):
    N = int(input())
    arr = list(map(int, input().split()))
    for _ in range(N):                           # 이 모든 걸 dump 수만큼 반복하기
        max_idx = arr.index(max(arr))            # 최대값, 최소값 인덱스 구하기
        min_idx = arr.index(min(arr))
        arr[max_idx] -= 1                        # 최대값에서는 1을 빼고, 최소값에서는 1을 더하기
        arr[min_idx] += 1
    a = max(arr)-min(arr)                        # dump 횟수만큼 반복 후 최대값과 최소값 차이 구하기
    print(f'#{i} {a}')

# 내장함수 안 쓰고 코드 쓰는거 연습 따로 해보기.
# max_idx = 0
# min_idx = 0
# for h in range(len(arr)):
#     if arr[max_idx] < arr[h]:
#         max_idx = h
# for l in range(len(arr)):
#     if arr[min_idx] > arr[l]:
#         min_idx = l