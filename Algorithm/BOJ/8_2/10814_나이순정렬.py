# 8/13. 실버5. 10814. 나이순 정렬. 나동빈 파일 문제
# 이거는 sort 이용하는 건데, key값을 이용해야함
# sorted로도 가능함
# 둘의 차이점을 알아놔야 하는데, sort는 반환하는거 아님. 그리고 key값만 적으면됨
# sorted는 반환하는 거라서 반환받을 변수 입력해야 함. 그리고 sorted() 괄호 안에 정렬할거 적어야함


N = int(input())

list1 = []
for i in range(N):
    a, b = list(input().split())
    list1.append((int(a), b))
list1.sort(key=lambda x: x[0])
# list1 = sorted(list1, key=lambda x: x[0])
for i in list1:
    print(i[0], i[1])