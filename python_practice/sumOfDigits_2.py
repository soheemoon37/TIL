# 각자리 숫자 합하기 2번째 방법

num = int(input())

def sumOfDigits(num):
    b = list(map(int, list(str(num))))
    return sum(b)

print(sumOfDigits(num))