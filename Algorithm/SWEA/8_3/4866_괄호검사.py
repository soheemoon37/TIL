import sys

sys.stdin = open("4866_괄호검사.txt")

# a로만 for문 이용했었는데, index가 적용이 잘 안됐음. pop 하니까 요소들이 지워져서
# 그래서 a를 복사해서 c를 만들어놓고 구현함
# sta 빈리스트 만들어놓고 isprint = False 로 설정해놓음
# c에 있는 괄호들 이제부터 적용할거임
# 먼저 {, ( 일때는 그냥 어펜드함
# }, ) 일때는 sta가 비어있는지 요소가 있는지 확인한 후에 -1번째가 {인지 (인지 확인해야함
# (를 확인안하니까 1개 틀려서 fail 나옴
# sta에 없을 때는 0임
# for문 다 돌리고 나서 isprint = False 인 경우 비교해서 프린트

T = int(input())
for _ in range(1, T + 1):
    a = list(input())
    b = ['{', '}', '(', ')']
    c = a[:]
    for i in a:
        if i not in b:
            c.pop(c.index(i))

    sta = []
    isprint = False
    for i in c:
        if i == '{' or i == '(':
            sta.append(i)
        elif i == '}':
            if sta:
                if sta[-1] == '{':
                    sta.pop()
                else:
                    print(f'#{_} 0')
                    isprint = True
                    break
            else:
                print(f'#{_} 0')
                isprint = True
                break
        elif i == ')':
            if sta:
                if sta[-1] == '(':
                    sta.pop()
                else:
                    print(f'#{_} 0')
                    isprint = True
                    break
            else:
                print(f'#{_} 0')
                isprint = True
                break

    if isprint == False:
        if sta:
            print(f'#{_} 0')
        else:
            print(f'#{_} 1')