# 각자리 숫자 합하기 sumOfDigits()

num = int(input())


def sumOfDigits(num):
    a = str(num)
    c = []
    c.extend(a)
    total = 0
    for i in c:
        total += int(i)
    return total

print(sumOfDigits(num))

# 아놔... extend 안쓰고 그냥 list하면 흩뿌려짐 ...
# for i in list(str(num)) 그냥 이러면 됨...
