N, M = list(map(int, input().split()))
a = []
for i in range(1, N+1): # N의 공약수 구하기
    if N % i == 0:
        a.append(i)
b = []
for j in range(1, M+1): # M의 공약수 구하기
    if M % j == 0:
        b.append(j)
c = set(a) & set(b) # 두 수의 최대공약수구하기
d = max(c)
print(max(c))
e = d * (N // d) * (M // d) # 두 수의 최소공배수 구하기
print(e)