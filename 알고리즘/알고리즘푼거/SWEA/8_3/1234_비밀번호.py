import sys

sys.stdin = open("1234_비밀번호.txt")

for _ in range(1, 11):
    A, B = input().split()
    a = list(map(int, B))
    sta = []
    for i in range(int(A)):
        if sta:
            if sta[-1] != a[i]:
                sta.append(a[i])
            else:
                sta.pop()
        else:
            sta.append(a[i])
    print(f'#{_}', end=" ")
    for i in sta:
        print(i, end='')
    print()