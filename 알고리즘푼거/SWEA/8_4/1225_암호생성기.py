
# 맨앞을 pop 하니까 저절로 인덱스가 앞으로 밀림
# 그러고 뒤에 어펜드 해줬음
# 잘 안되다가 while 안에 if문으로 a-i 가 0보다 작거나 가을 때 break 하라고 하니까 됐음

for _ in range(1, 11):
    N = int(input())
    arr = list(map(int, input().split()))
    print(f'#{_}', end=' ')
    while arr[-1] > 0:
        for i in range(1, 6):
            a = arr.pop(0)
            arr.append(a-i)
            if a-i <= 0:
                arr[-1] = 0
                break
    for i in arr:
        print(i, end=' ')
    print()

