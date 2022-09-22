T = int(input())
for _ in range(1, T+1):
    a = list(input())
    a_list = []
    while a:
        b = ''
        for i in range(7):
            c = a.pop(0)
            b += c
        a_list.append(b)
    for i in a_list:
        total = 0
        for j in range(7):
            total += int(i[j]) * (2 ** (6-j))
        print(total, end=' ')
    print()
