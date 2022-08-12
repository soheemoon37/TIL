import sys

sys.stdin = open("14425_문자열집합.txt")

# 먼저 N 과 M 만큼의 리스트를 각각 만들고, 값 어펜드하기
# list2에 있는 값이 list1에 있으면 count +1 하기

N, M = list(map(int, input().split()))
list1 = []
list2 = []
for n in range(N):
    a = input()
    list1.append(a)
for m in range(M):
    b = input()
    list2.append(b)
count = 0
for i in list2:
    if i in list1:
        count += 1
print(count)
