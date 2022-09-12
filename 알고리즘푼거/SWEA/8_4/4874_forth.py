

# 아 이거 먼저 pop 한 거를 뒤에 써야되네??ㅋㅋㅋ 그거때문에 계속 헤맸음
# '/' 랑 '-'는 민감함..ㅋㅋㅋ

T = int(input())
for _ in range(1, T+1):
    arr = list(input().split())
    sta = []
    isprint = False
    for i in arr:
        if i.isdecimal():                 # 숫자가 들어오면 스택에 추가
            sta.append(int(i))

        else:
            if i == '*' and len(sta) >= 2:
                a = sta.pop()
                b = sta.pop()
                sta.append(a * b)
            elif i == '+' and len(sta) >= 2:
                c = sta.pop()
                d = sta.pop()
                sta.append(c + d)
            elif i == '-' and len(sta) >= 2:
                e = sta.pop()
                f = sta.pop()
                sta.append(f - e)
            elif i == '/' and len(sta) >= 2:
                g = sta.pop()
                h = sta.pop()
                if h != 0:
                    sta.append(h // g)
            elif i == '.' and len(sta) == 1:  # sta 에 1개만 남아있어야함
                if isprint == False:
                    print(f'#{_} {sta[0]}')
            else:                             # 나머지 경우는 다 에러
                isprint = True
                print(f'#{_} error')
                break
