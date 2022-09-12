'''실버4. 이진탐색이용하는 문제임
덕분에 이진탐색 다시 공부했음
이거 처음에 그냥 in 사용했는데 시간초과떴음'''

import sys
input = sys.stdin.readline

def bs(arr, N, key):
    s = 0
    e = N - 1
    while s <= e:
        center = (s+e) // 2
        if key == arr[center]:
            return 1
        elif key > arr[center]:
            s = center + 1
        elif key < arr[center]:
            e = center - 1
    return 0


N = int(input())
arr = list(map(int, input().split()))
arr.sort()
M = int(input())
arr2 = list(map(int, input().split()))

for i in range(M):
    print(bs(arr, N, arr2[i]))

