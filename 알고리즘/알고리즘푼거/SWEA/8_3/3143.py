import sys

sys.stdin = open("3143.txt")

# 공백으로 replace해서 한글자로 치면 됨.
# 공백 자리에 a라고 적었었는데 준봉이가 공백으로 놔두는게 좋다고 함
# 왜냐면 문자로 두면 논란의 여지가 있을듯... 공백도 한 자리로 치니까 공백으로 놔두는 게 나은듯
# 열받는 게 이 문제를 저번시간에 했던 bruteforce함수로 했는데
# 계속 안 나와서 1시간 동안 헤맸거든? 근데 브루트포스는 잘은 모르겠는데 문제가있었음

T = int(input())
for test_case in range(1, T+1):
    A, B = input().split()
    C = A.replace(B, ' ')
    print(f'#{test_case} {len(C)}')