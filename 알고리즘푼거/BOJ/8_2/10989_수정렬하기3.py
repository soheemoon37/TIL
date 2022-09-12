# 8/13. 10989. 수정렬하기3. 브론즈1
# 웬만한 방법으로 풀면 거의 시간초과뜸
# 이 방법만 되는듯? 이 방법을 이제야 처음으로 알았음..
# 내장함수를 써야 메모리를 덜 잡아먹어서 시간초과가 안되는 경우가 많나봄
# 찾아보니 input()속도가 느린거면 sys 라이브러리 내장함수 이용해야 하나봄

import sys

n = int(sys.stdin.readline())
array = [0] * 10001

for i in range(n):
    data = int(sys.stdin.readline())
    array[data] += 1

for i in range(10001):
    if array[i] != 0:
        for j in range(array[i]):
            print(i)
