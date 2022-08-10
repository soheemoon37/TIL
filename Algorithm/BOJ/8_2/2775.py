# 8월 10일. 브론즈1. 부녀회장이 될테야
# 아놔 2시간 가까이 푼듯?? 계속 답 막 반복되게 나와서 포기할 뻔...
# 이거 나는 apart 층이랑 거주자 수를 다 구해놓고 찾는 걸로 풀었음.
# 이거 막 append 위치랑 이런거 잘 조정해야 됨. 계속 이상하게 나와서 진땀뺌

import sys

sys.stdin = open("2775.txt")

T = int(input())
for test_case in range(T):
    k = int(input())
    n = int(input())
    apart = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]]
    for i in range(1, 15):
        list_a = [0] * 14
        value = 0
        for c in range(14):
            value += apart[i-1][c]
            list_a[c] = value
        apart.append(list_a)
    print(apart[k][n-1])




