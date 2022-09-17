# 후위순회
def postorder(n):
    if n:
        postorder(ch1[n])
        postorder(ch2[n])
        postfix.append(tree[n])

for _ in range(1, 11):
    print(f'#{_}', end=' ')
    V = int(input())
    ch1 = [0] * (V + 1)
    ch2 = [0] * (V + 1)
    tree = [0] * (V + 1)
    for i in range(1, V+1):
        a = list(input().split())
        if a[1].isdecimal():
            tree[i] = int(a[1])
        else:
            tree[i] = a[1]
        if len(a) == 4:  # 연산자 경우 자식들 저장
            ch1[i] = int(a[2])
            ch2[i] = int(a[3])

    postfix = []
    postorder(1)

    sta = [] # 계산기 이용
    for i in postfix:
        # 여기서 str 안 붙이니까 안나옴.. i가 숫자라서 str 붙여서 판단
        # 숫자랑 비슷한 애들은 어펜드함
        if str(i).isdigit():
            sta.append(i)
        else:
            b = sta.pop()
            a = sta.pop()
            if i == '+':
                sta.append(a+b)
            elif i == '-':
                sta.append(a-b)
            elif i == '*':
                sta.append(a*b)
            elif i == '/':
                sta.append(a/b)
    print(int(sta[-1]))
