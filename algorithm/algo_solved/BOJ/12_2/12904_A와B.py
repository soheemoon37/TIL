a = list(input())
b = list(input())

# 마지막이 A 일때는 pop 하고 B 일때는 pop 하고 뒤집기
for i in range(len(b)-len(a)):
    if b[-1] == 'A':
        b.pop(-1)
    elif b[-1] == 'B':
        b.pop(-1)
        b = b[::-1]
    if b == a:
        print(1)
        break
else:
    print(0)