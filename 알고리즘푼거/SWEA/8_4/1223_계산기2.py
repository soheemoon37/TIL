
# sta, sta1 리스트 각각 만들어서 sta2 에 숫자넣고 pop 된 연산자들 넣을거임
# '*' 랑 '+' 밖에서 없어서 각각 경우의 수 나눠서 sta1 리스트 만들기. 이거는 후위표기법한 거임

for _ in range(1, 11):
    N = int(input())
    arr = list(input())
    sta = []
    sta1 = []
    print(f'#{_}', end=' ')

    for i in arr:
        if 48 <= ord(i) <= 57:                       # ord 이용해서 숫자일때는 그냥 출력
            sta1.append(i)

        else:
            if i == '*':
                while sta:
                    if sta[-1] == '+':
                        break
                    else:
                        sta1.append(sta.pop())
                sta.append(i)

            elif i == '+':
                while sta:
                    if not sta:
                        break
                    else:
                        sta1.append(sta.pop())
                sta.append(i)
    if sta:
        for i in range(len(sta) - 1, -1, -1):  # sta 에 뭐가 남아있으면 뒤에서부터 출력, pop 해서 출력해도됨
            sta1.append(sta[i])

# 여기부터는 계산기할거임
# sta2 만들어놓고 숫자면 그냥 추가하기
# '*' 나 '+' 이거면 계산한 값을 sta2에 추가하기. 이때 a,b 순서 고려해야됨. 먼저 나온게 앞에있기
    sta2 = []
    for i in sta1:
        if 48 <= ord(i) <= 57:
            sta2.append(int(i))
        elif i == '*':
            a = sta2.pop()
            b = sta2.pop()
            sta2.append(a * b)
        elif i == '+':
            c = sta2.pop()
            d = sta2.pop()
            sta2.append(c + d)
    print(sta2[0])
