# 8월 13일. 실버3. 팰린드롬만들기. 1213번
# 와. . .푸는데 2시간 넘게 걸린듯? 아놔 ㅋㅋㅋㅋㅋ

# 입력값을 먼저 리스트로 만드는 데 딕셔너리만들기위해서 반복되는 거는 지우려고 set썼음
# 알파벳 순으로 하라해서 sort하고 딕셔너리에 알파벳 각각 몇개인지 넣고 딕셔너리 만듬

list1 = list(input())
list2 = list(set(list1))
list2.sort()
dict1 = {}
for i in range(len(list2)):
    dict1[list2[i]] = 0

for i in range(len(list1)):
    dict1[list1[i]] += 1

# 이거 일단은 홀수, 짝수 나눠서 해야됨
# 나는 반반 나눠서 했기 때문에 일단 짝수일때는 반 나눈거 만큼 리스트에 넣기
# 홀수일 때도 똑같은데, 딕셔너리 밸류값에 1이 남아있을 거임
list3 = []
for i in range(len(dict1)):
    if dict1[list2[i]] % 2 == 0:
        list3.append(list2[i] * (dict1[list2[i]] // 2))
        dict1[list2[i]] -= ((dict1[list2[i]] // 2) * 2)
    elif dict1[list2[i]] % 2 == 1 and dict1[list2[i]] != 1:
        list3.append(list2[i] * (dict1[list2[i]] // 2))
        dict1[list2[i]] -= ((dict1[list2[i]] // 2) * 2)

# 이게 그 다음이 좀 애매했는데, 일단 밸류값을 total했을 때를 정해놓고
# 경우를 나눠야 했음
# total이 0일 때는 아무 문제 없으니까 그냥 넘어가기
# total이 1일 때는 그 알파벳을 추가해야됨
# total이 1보다 클 때는 회문 안되는 경우라서 저렇게 프린트해주고 break함
# 이 부분에서 오류가 좀 많이 남...
# if랑 elif 잘 사용해야됨
total = 0       
for i in range(len(dict1)):
    total += dict1[list2[i]]
    if total == 0:
        pass
    elif total == 1:
        for c in range(len(dict1)):
            if dict1[list2[i]] == 1:
                list3.append(list2[i])
                dict1[list2[i]] -= 1
    elif total > 1:
        print("I\'m Sorry Hansoo")
        break

# 그 다음은 join 이용해서 문자결합하면 되는데
# 처음에 if문 안 이용하니까 total이 1보다 클 때 문제가되었음
# 그래서 초반에 if문으로 놔두고 문자열들 결합함
if total == 0 or total == 1:
    a = ''.join(list3)
    if total == 1:   
        list3.pop()
    list3.sort(reverse=True)
    b = ''.join(list3)
    print(a+b)

