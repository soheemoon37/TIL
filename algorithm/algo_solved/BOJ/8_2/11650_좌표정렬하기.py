# 8/13. 11650. 실버5. 좌표정렬하기
# 아까 나동빈 파일에 첫번째 문제랑 조금 헷갈렸음
# 첫번째 문제는 나이 동일하면 먼저 입력된 이름 순서라고 key값을 따로 설정해줬음
# 그렇게 안 하면 이름도 알파벳순으로 되어버림
# 근데 이번 문제는 굳이 key값 설정안해도 숫자 순서대로 나옴


N = int(input())
list1 = []
for _ in range(N):
    list2 = list(map(int, input().split()))
    list1.append(list2)

list1.sort()
for i in range(len(list1)):
    print(list1[i][0], list1[i][1])

