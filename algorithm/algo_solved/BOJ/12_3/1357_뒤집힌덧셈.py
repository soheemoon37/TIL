a, b = input().split()

a = list(a)
b = list(b)

# 문자열 뒤집기
a = a[::-1]
b = b[::-1]

# 앞에 0 올 때, 0 없애기
while len(a) > 0:
    if a[0] == '0':
        a.pop(0)
    else:
        break
while len(b) > 0:
    if b[0] == '0':
        b.pop(0)
    else:
        break
    
# join 해서 숫자로 만든후, 더하고 더한값 프린트하기
a = int(''.join(a))
b = int(''.join(b))
c = str(a + b)
c = c[::-1]
c = int(''.join(c))
print(c)