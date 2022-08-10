import sys

sys.stdin = open("0810_p2.txt")

T = int(input())
for test_case in range(1, T+1):
    arr = list(map(int, input().split()))
    n = len(arr)
    b = []
    for i in range(1<<n): # 비트연산자 이용해서 부분집합 구하기
        a = []
        for j in range(n):
            if i & (1<<j):
                a.append(arr[j])
        if a: # 공집합은 빼기
            b.append(a)
    for i in range(len(b)): # 각 부분집합의 합을 구하기
        h = sum(b[i])
        if h == 0: # 합이 0이면 1 출력
            print(f'#{test_case} 1')
            break
    if h != 0: # 그렇지 않은 경우는 0 출력
        print(f'#{test_case} 0')