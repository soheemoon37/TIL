# 8/21. 실버5.
# 이거 다 1때문이야 ㅠㅠㅠㅠㅠㅠㅠㅠㅠ
# 계속 틀리고, 런타임에러 뜨고 힝
# 1이 문제였고, 슬라이스써서 런타임에러 뜬거같은데 이거는 set로 바꿔서 괜찮아짐
# 이거 일단 숫자를 0부터 계속 더해줬음
# 그러다가 total값이랑 S가 같거나 total이 더 커지면 break
# S가 1일때를 따로 if문으로 걸어놨음
# 나머지 경우에서는 0까지 더한거라서 -2, -1 해줌
# 넘치는거는 어쩔수 없이 같은 자연수를 더할 수 밖에 없어져서
# 그냥 list1 len에서 0값이랑 마지막 값을 빼주면됨.


S = int(input())

total = 0
cnt = 0
list1 = []
for i in range(S):
    total += i
    cnt += 1
    list1.append(i)
    if total >=  S:
        list1.pop()
        list1.append(S - sum(list1))
        break
if S == 1:
    print(1)
else:
    if len(list1) != len(set(list1)):
        print(len(list1)-2)
    else:
        print(len(list1)-1)
