# 2인 거를 계속 빼주면서 5로 나누어떨어질때를 구해주면됨

a = int(input())

num = 0
while a >= 0:
    if a % 5 == 0:
        num += a // 5
        print(num)
        break
    a -= 2
    num += 1
else:
    print(-1)
