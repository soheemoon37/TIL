# 타일링 방법을 알면 바로 풀 수 있는 문제!

n = int(input())

dp = [1, 2, 3]
for i in range(3, 1000):
    dp.append(dp[i-2] + dp[i-1])

print(dp[n-1]%10007)