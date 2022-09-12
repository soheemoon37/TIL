import sys

sys.stdin = open("4837_부분집합의합.txt")

T = int(input())
for test_case in range(1, T+1):
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    N, K = list(map(int, input().split()))
    n = len(arr)
    b = []
    for i in range(1<<n): # 비트연산자 이용해서 부분집합 구하기
        a = []
        for j in range(n):
            if i & (1<<j):
                a.append(arr[j])
        if a:  # 공집합은 빼기
            b.append(a)
    count = 0
    for i in range(len(b)): # 부분집합의 길이와 합을 각각 n, k로 두기
        n = len(b[i])
        k = sum(b[i])
        if n == N and k == K: # n, k 값이 입력값과 같다면 count에 1더하기
            count += 1
    if count >= 1: # count가 값이 있으면 count 출력
        print(f'#{test_case} {count}')
    else:
        print(f'#{test_case} 0')