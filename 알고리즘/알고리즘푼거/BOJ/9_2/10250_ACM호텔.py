'''브론즈 2 주제에 왜 어려움?ㅋㅋㅋ 나만어려웠나봄
나는 일단 B로 놔두고 그기에 번호를 채웠음
근데 아래층부터 쌓이니까 리버스해주고 또 역순으로 차례로 나열해서
1차원 리스트로 만들어서 N 값 넣어서 출력함'''

# 방법1
NUM = int(input())
for _ in range(NUM):
    H, W, N = map(int, input().split())
    B = [[0] * W for _ in range(H)]
    for i in range(H):
        for j in range(W):
            if j+1 < 10:
                B[i][j] = str(H-i) + str(0) + str(j+1)
            else:
                B[i][j] = str(H-i) + str(j+1)
    B.reverse()
    B1 = []
    for i in range(W):
        for j in range(H):
            B1.append(B[j][i])
    # print(B1)
    print(B1[N-1])

# 방법2 승태랑 수학적으로 같이 푼거~~ 이거 더 어려븐거같음
NUM = int(input())
for _ in range(NUM):
    H, W, N = map(int, input().split())
    # 6 12 10
    if N % H == 0:
        if (N // H) < 10:
            print(str(H) + str(0) + str((N // H)))
        else:
            print(str(H) + str((N // H)))
    else:
        if (N // H) + 1 < 10:
            print(str(N % H) + str(0) + str((N // H)+1))
        else:
            print(str(N % H) + str((N // H)+1))

