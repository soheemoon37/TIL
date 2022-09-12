import sys

sys.stdin = open("4873_반복문자지우기.txt")

# 스택 이용함
# 빈리스트 만들어놓고 입력값의 처음 문자를 어펜드해놓기
# sta에 요소가 있는 경우와 없는 경우를 나누어놓음
# sta 마지막 요소와 같지 않으면 어펜드하고 아니면 팝하고 continue하기
# sta 가 비어있으면 그냥 어펜드하기

T = int(input())
for _ in range(1, T+1):
    a = input()
    sta = []
    sta.append(a[0])
    for i in range(1, len(a)):
        if sta:
            if a[i] != sta[-1]:
                sta.append(a[i])
            else:
                sta.pop()
                continue
        else:
            sta.append(a[i])
    print(f'#{_} {len(sta)}')


