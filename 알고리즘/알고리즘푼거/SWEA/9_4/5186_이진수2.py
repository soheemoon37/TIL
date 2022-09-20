
T = int(input())
for _ in range(1, T+1):
    print(f'#{_}', end=' ')
    N = float(input())
    output = ''
    while N:
        output += str(int((N * 2)))
        N = float(N * 2) - int(N * 2)
    if len(output) >= 13:
        print('overflow')
    else:
        print(output)