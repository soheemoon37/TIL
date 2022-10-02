'''실버1. 코드를 보면 쉬운데 나는 지금 실력으론 못품
T, F 를 이용해서 풀고있고, array 랑 dp 랑 헷갈림
그리고 연주가 안 되는 경우에 -1 출력이라 마지막에
result 를 -1로 지정해놓고 출력구한다는 점도 기억해놓기'''


# N 개의 곡, 시작볼륨 S, 최대볼륨 M
# 3 5 10
# 5 3 7
n, s, m = map(int, input().split())
array = list(map(int, input().split()))

dp = [[0] * (m+1) for _ in range(n+1)]
dp[0][s] = 1

for i in range(1, n+1):
    for j in range(m+1):
        if dp[i-1][j] == 0:
            continue
        if j - array[i-1] >= 0:
            dp[i][j-array[i-1]] = 1
        if j + array[i-1] <= m:
            dp[i][j+array[i-1]] = 1

result = -1
for i in range(m, -1, -1):
    if dp[n][i] == 1:
        result = i
        break
print(result)


