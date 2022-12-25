# 파이썬으로는 시간초과, 파이파이는 됨

a, b = input().split()

total = 0
for i in range(len(a)):
    for j in range(len(b)):
        total += int(a[i]) * int(b[j])

print(total)

# 숫자 다 더해서 곱하면 됨 !!

a, b = input().split()

a = list(map(int, a))
b = list(map(int, b))

print(sum(a)*sum(b))

