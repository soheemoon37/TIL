
# 팩토리얼 구하기
def f(n):
    if n <= 1:
        return 1
    else:
        return n * f(n-1)

a = f(int(input()))
a = str(a)  # 문자로 만든 후 뒤집기
a = a[::-1]
cnt = 0
i = 0
while True:  # 0 개수 세기
    if a[i] != '0':
        break
    else:
        cnt += 1
        i += 1
print(cnt)
