'''이게 내가 순열 코드 잘 몰라서 인덱스 헷갈림..
일단 아이디어는 앞이랑 뒤는 0 으로 남겨놓고 나머지 인덱스를 이용할거임'''

def f(i, k):
    global minV
    if i == k:
        total = 0
        # 토탈 다 더해서 minV 값이랑 비교해서 제일 작은 값 구하기
        for i in range(1, N+1):
            total += arr[p[i-1]][p[i]]
        if total < minV:
            minV = total
    else:
        for j in range(1, k):
            if used[j] == 0:
                used[j] = 1
                p[i] = a[j]
                f(i+1, k)
                used[j] = 0


T = int(input())
for _ in range(1, T+1):
    print(f'#{_}', end=' ')
    N = int(input())
    arr = [list(map(int, input().split())) for i in range(N)]
    a = [i for i in range(N)]  # p 의 인덱스를 쓸 거라 0부터 시작하도록 설정
    used = [1] + ([0] * (N-1)) # 0 은 계속 그대로 놔두려고 used 1로 설정해놓기
    p = [0] * (N+1)  # 맨 마지막 0으로 놔두려고 (N+1) 만큼 설정
    minV = 10000000  # 임의의 minV 값 정해놓기
    f(1, N)
    print(minV)
