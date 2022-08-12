import sys

sys.stdin = open("1221_GNS.txt")

# 딕셔너리로 풀었음.
# 사실 권민이한테 배워옴
# 딕셔너리 만들어놓고, 딕셔너리 키 값의 밸류를 키 값이 나올 때마다 하나씩 올려줌
# 그러고 딕셔너리에서 키, 밸류 값에서 밸류 값만큼 반복을 해서 키 값을 출력해줌
# 여기서 end를 이용해서 공백 만들고, test_case 마다 문단바꾸기 위해서 print() 적어줌
# 그리고 #1 이런식으로 써야 하니까 위에 print(N)으로 써놔주기

T = int(input())

for test_case in range(1, T+1):
    dict1 = {"ZRO" : 0, "ONE" : 0, "TWO" : 0, "THR" : 0, "FOR" : 0, "FIV" : 0, "SIX" : 0, "SVN" : 0, "EGT" : 0, "NIN" : 0}
    N, M = list(input().split())
    print(N)
    list1 = list(input().split())
    for i in range(len(list1)):
        dict1[list1[i]] += 1
    for k, v in dict1.items():
        for val in range(v):
            print(k, end=" ")
    print()

