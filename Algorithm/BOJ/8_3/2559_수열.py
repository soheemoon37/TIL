# 8/21. 실버3.
# 하.. 문제답은 쉽게 나오는데 계속 시간초과뜸 ㅋㅋㅋㅋ
# sum이 시간을 많이 잡아먹나봄
# 그래서 리드라인 썼는데 그래도 시간초과임
# 결국 구글링함. 결과.. 왜그런지는 아직 잘 모르겠지만
# sum을 덜하게 만들수 있는 방법이 맨 처음에 미리 더해놓고
# 그 값을 이용해서 다음수를 더하고 앞에 값의 맨 앞은 빼고
# 이런식으로 썼음. 그러면 sum을 여러번 반복안해도 되서 그런건지
# 시간이 단축됨


import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))

total1 = sum(arr[:M])

list1 = [sum(arr[:M])]
for i in range(1, N-M+1):
    total_tem = list1[-1] + arr[i+M-1] - arr[i-1]
    list1.append(total_tem)
print(max(list1))