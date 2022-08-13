# 8월 13일. 실버4. 제로. 10773
# 스택구조라서 pop 이용하는 문제
# 0이 아니면 어펜드하고 0이면 list에 있는 수를 팝하면 됨

N = int(input())
list1 = []
for i in range(N):
    a = int(input())
    if a != 0:
        list1.append(a)
    if a == 0:
        list1.pop()
if list1:
    print(sum(list1))
else:
    print(0)