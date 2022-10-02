'''LCS 문제는 두 수열이 주어졌을 때, 모두의 부분 수열이 되는
수열 중 가장 긴 것을 찾는 문제이다.
완전 dp 문제이고, 문제 이해를 잘 해야함
계속 쌓아가면서 답을 구하는 거라서 다시 보고 이해하시고
골드5'''

x = input()
y = input()

dp = [[0] * (len(y) + 1) for _ in range(len(x) + 1)]

for i in range(1, len(x) + 1):
    for j in range(1, len(y) + 1):
        if x[i-1] == y[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i][j-1], dp[i-1][j])

print(dp[len(x)][len(y)])