import sys

sys.stdin = open("1220_마그네틱.txt")

# stack 이용
# 일단 열의 행렬 만들기 arr3
# 여기서 고려해야 할거는 1이 먼저 들어가있을 때, 2가 들어가면 cnt를 세는거임
# 원래는 sta에 pop을 했었는데 그렇게 안해도됨
# 1122이럴 때 카운트가 2번이 되어버림
# 그래서 그냥 계속 추가하면서 카운트세면되고
# 여기서 숫자가 크게 나와서 디버깅 해보니까 cnt 를 cnt_list 에 추가할 때
# for문에 맞춰 적어야 하는데 그렇게 안해서 잘못나온거
# 맞춰쓰는거 연습하세요
# 그리고 cnt랑 sta는 계속 리셋해줘야 함

for _ in range(1, 11):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    arr3 = []
    for i in range(100):
        arr2 = []
        for j in range(100):
            arr2.append(arr[j][i])
        arr3.append(arr2)

    cnt_list = []
    for i in range(100):
        cnt = 0
        sta = [0]
        for j in range(100):
            if arr3[i][j] == 1:
                sta.append(arr3[i][j])
            elif arr3[i][j] == 2:
                if sta[-1] == 1:
                    sta.append(arr3[i][j])
                    cnt += 1
        cnt_list.append(cnt)
    print(f'#{_} {sum(cnt_list)}')



