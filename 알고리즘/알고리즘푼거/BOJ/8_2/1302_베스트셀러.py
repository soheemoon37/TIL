# 8월 13일. 1302. 실버4. 베스트셀러
# 먼저 중복되지 않는 키 값을 위해 set를 이용해서 list만들기
# 딕셔너리 만들어서 count 세기
# 딕셔너리의 밸류 값이 중요하니까 밸류값 크기순서대로 정렬
# 밸류 값 같은 거 있는지 확인해서 리스트에 모으고
# 알파벳으로 정렬한 후 제일 앞에 값 출력

N = int(input())
list1 = []
for i in range(N):
    list1.append(input())
list2 = list(set(list1))

dict1 = {}
for i in range(len(list2)):
    dict1[list2[i]] = 0

count = 0
for i in range(len(list1)):
    dict1[list1[i]] += 1

list3 = []
for k, v in dict1.items():
    list3.append((v, k))

list3.sort(reverse = True)

list4 = []
list4.append(list3[0][1])

for i in range(1, len(list3)):
    if list3[i][0] == list3[0][0]:
        list4.append(list3[i][1])

list4.sort()
print(list4[0])