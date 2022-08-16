import sys

sys.stdin = open("4861_회문.txt")

# 아 이거는 일단 세로로도 회문이 찾아지 수 있다 해서 열의 리스트를 arr3로 만들어놓고
# M이 N이랑 같을 때랑 더 작을 때를 나눠서 비교했음
# 같은 경우는 크게 상관없는데, 다를 경우에는 for 문 한 번 더 썼음
# N-M+1까지만 비교를 해야하고 arr[i][j:j+M]이런식으로 리스트안에서 어디부터 어디까지 정해서 회문 살펴봐야함

T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]
    arr3 = []
    for j in range(N):
        arr2 = []
        for i in range(N):
            arr2.append(arr[i][j])
        arr3.append(arr2)

    if N == M:
        for i in range(N):
            if arr[i] == arr[i][::-1]:
                a = ''.join(arr[i])
                print(f'#{test_case} {a}')
        for i in range(N):
            if arr3[i] == arr3[i][::-1]:
                a = ''.join(arr3[i])
                print(f'#{test_case} {a}')
    if N > M:
        for i in range(N):
            for j in range(N-M+1):
                if arr[i][j:j+M] == arr[i][j:j+M][::-1]:
                    a = ''.join(arr[i][j:j+M])
                    print(f'#{test_case} {a}')
        for i in range(N):
            if arr3[i][j:j+M] == arr3[i][j:j+M][::-1]:
                a = ''.join(arr3[i][j:j+M])
                print(f'#{test_case} {a}')