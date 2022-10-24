a = int(input())
b = int(input())

a = a//100
a = a*100

while True:
    if a % b == 0:
        break
    else:
        a += 1
a = str(a)
print(a[-2:])