n, m = map(int, input().split())

time = list(map(int, input().split()))
time.sort(reverse=True)                  # 큰 순서로 정렬
q = [0] * m                              # 충전기 수만큼 만들어놓기

# 제일 작은 충전기에다 계속 시간 더하기
i = 0
while i < n:
    j = q.index(min(q))
    q[j] += time[i]
    i += 1

# 충전 시간 제일 긴 충전기 고르기
print(max(q))