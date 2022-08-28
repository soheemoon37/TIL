'''브론즈2 주제에 시간좀걸림...
이거 피타고라스 정리 이용해서 계속 계산해나갔고
루트할때 괄호 쳐야 되는거 알아두기'''

D, H, W = map(int, input().split())
D = D * D
C = D / ((H / W) ** 2 + 1)
b = (D / ((H / W) ** 2 + 1)) ** (1/2)
a = H / W * b
print(int(a), end=' ')
print(int(b))

