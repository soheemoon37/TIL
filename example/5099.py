import sys
sys.stdin = open("a.txt")

T = int(input())
for _ in range(1, T+1):
    N, M = map(int, input().split())
    plate = []
    pizza = list(map(int, input().split()))
    pizza1 = []
    for val in enumerate(pizza):
        pizza1.append(list(val))

    for i in range(N):
        plate.append(pizza1.pop(0))

    while len(plate) > 1:
        print(plate)
        if plate[0][1] == 0:     # 반갈죽해서 맨앞에 왔는데 0이 되면 그냥 pop 해버림
            plate.pop(0)
            if len(pizza1) >= 1:    # 남은 피자가 있으면
                plate.append(pizza1.pop(0))        # 플레이트에 넣어줌
            else:
                continue
        else:   # 반갈죽해서 뒤로 보내는거
            plate[0][1] = plate[0][1] // 2
            plate.append(plate.pop(0))

            # 반갈죽 한 다음에 판단을 하는거지
            # 반갈죽 한 게 1일 경우
            # 만약 남은피자가 있을때 / 없을때
            # 반갈죽 한 게 1이 아닐 경우
            # 1이 아니면 뒤로 보내겠지?
            # 뭐 이정도?
    print(f'#{_} {plate[0][0]+1}')


