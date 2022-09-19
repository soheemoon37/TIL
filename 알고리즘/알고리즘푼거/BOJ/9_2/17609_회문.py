# 골드5. 한 5시간동안 연구한듯.
# 결국 구글링함 ㅋㅋㅋㅋㅋ
# 함수 2개 썼고, 내가 생각한 방법으로는 답은 나오는데 시간초과임


# 회문인지 아닌지 체크하는 함수 구현
# 두 포인터로 놔두고 왼쪽은 하나씩 올리고, 오른쪽은 내리면서 비교
def check(left, right):
    while left < right:
        if a[left] == a[right]:
            left += 1
            right -= 1
        else:
            return False
    return True

# 이거는 문자 빼서 보려고 넣는 함수
# if 에서 문자열비교하다가 안되면 else 구문으로 넘어감
# 왼쪽이나 오른쪽에서 하나씩 빼서 남는 거 회문인지 체크
# 회문이면 1 리턴하고 아니면 2 리턴하기
# while 문 다 돌아서 둘 다 아니면 회문이니까 0 리턴하기

def twopointer(left, right):
    while left < right:
        if a[left] == a[right]:
            left += 1
            right -= 1
        else:
            if check(left+1, right) or check(left, right-1):
                return 1
            else:
                return 2
    return 0


N = int(input())
for i in range(N):
    a = input()
    print(twopointer(0, len(a)-1))