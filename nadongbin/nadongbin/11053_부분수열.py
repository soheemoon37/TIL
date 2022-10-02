'''실버2. 이거도 dp. dp는 다른 인덱스값들을 이용해서
값을 가공하는 방법임. array 랑 dp 2개의 리스트를 쓰고
array 값이 크다면 본인값이랑 j 인덱스의 값에서 1 더한 값 중에
더 큰 값 고르면 됨'''
n = int(input())

array = list(map(int, input().split()))
# [10, 20, 10, 30, 20, 50]
dp = [1] * n
# [1, 1, 1, 1, 1, 1]
for i in range(1, n):
    for j in range(0, i):
        if array[j] < array[i]:
            dp[i] = max(dp[i], dp[j]+1)
print(max(dp))


