'''골드5번이고 나는 지금 실력으론 이해도 힘든 문제임
이중리스트로 dp 를 만들어놓고 중요한 포인트는 윗줄이랑 비교하는거임
else 구문에서 바로 위칸이랑 다른거 비교해서 max 값 추리는거 있는데
이거 j - weight 하는데 그게 이제 앞에서 미리 가치더해지는 거 있으면 + 되는거
3, 4 = 7 생각해보기'''


n, k = map(int, input().split())
dp = [[0] * (k+1) for _ in range(n+1)]

for i in range(1, n+1):
    weight, value = map(int, input().split())
    for j in range(1, k+1):
        if j < weight:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-weight] + value)
print(dp[n][k])