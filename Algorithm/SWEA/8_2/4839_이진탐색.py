import sys

sys.stdin = open("4839_이진탐색.txt")

def binary_search(a, N, key):
    start = 0
    end = N - 1
    count = 0
    while start <= end:                        # start 값이 end 값보다 작거나 같은 경우에서만 작동
        center = (start+end) // 2              # 중간값 정해두기
        if a[center] == key:                   # key 값이 중간값과 같은 경우 count 출력
            count += 1
            return count
        # 주의해야 할 부분!!! 원래 +1 했는데 문제 보니깐 center 값을 바로 end 값으로 설정하는듯
        # +1 하니깐 fail 나옴...
        elif a[center] > key:                  # key 값이 중간값보다 작은 경우 end 값을 center 값으로 바꿔주기(범위줄이기)
            count += 1
            end = center
        else:                                  # key 값이 중간값보다 작은 경우 start 값을 center 값으로 바꿔주기(범위줄이기)
            count += 1
            start = center
    return count


T = int(input())

for test_case in range(1, T+1):
    P, Pa, Pb = list(map(int, input().split()))
    a = list(range(1, P+1))
    # 함수 출력값을 비교해서 누가 이겼는지 구하기
    if binary_search(a, P, Pa) > binary_search(a, P, Pb):
        print(f'#{test_case} B')
    elif binary_search(a, P, Pa) < binary_search(a, P, Pb):
        print(f'#{test_case} A')
    else:
        print(f'#{test_case} 0')
