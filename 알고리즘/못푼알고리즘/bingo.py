'''첫번째 빙고 구현한건데 답 안 나옴'''

import sys
sys.stdin = open("a.txt")

bingo = []
for i in range(5):
    a = list(map(int, input().split()))
    bingo.append(a)

bingo2 = []
for i in range(5):
    b = []
    for j in range(5):
        b.append(bingo[j][i])
    bingo2.append(b)

number = []
for i in range(5):
    a = list(map(int, input().split()))
    for j in range(5):
        number.append(a[j])

cnt = 0
number2 = []
for i in range(25):
    for j in range(5):
        if cnt == 3:
            break

        cnt = 0
        if number[i] in bingo[j]:
            number2.append(number[i])
            bingo[j][bingo[j].index(number[i])] = 0
        for m in range(5):
            if bingo[m].count(0) == 5:
                cnt += 1
            else:
                break
        print(bingo)
        if number[i] in bingo2[j]:
            bingo2[j][bingo2[j].index(number[i])] = 0
        for s in range(5):
            if bingo2[s].count(0) == 5:
                cnt += 1
            else:
                break
        print(bingo2)
        if bingo[0][0] == bingo[1][1] == bingo[2][2] == bingo[3][3] == bingo[4][4] == 0:
            cnt += 1
        if bingo[0][4] == bingo[1][3] == bingo[2][2] == bingo[3][1] == bingo[4][0] == 0:
            cnt += 1

