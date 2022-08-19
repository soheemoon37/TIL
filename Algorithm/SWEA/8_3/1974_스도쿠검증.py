import sys

sys.stdin = open("1974_스도쿠검증.txt")

# arr 만들고, 세로열 arr3 만들고, 3 * 3 열 arr4 만들어놓기
# 중복되는 수만 없으면 되니까 set 이용했음

T = int(input())
for _ in range(1, T+1):
    arr = [list(map(int, input().split())) for _ in range(9)]
    arr3 = []
    for i in range(9):
        arr2 = []
        for j in range(9):
            arr2.append(arr[j][i])
        arr3.append(arr2)

    arr4 = []
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            arr5 = []
            for m in range(3):
                for n in range(3):
                    arr5.append(arr[i+m][j+n])
            arr4.append(arr5)

    list1 = []
    for i in range(9):
        if len(arr[i]) != len(set(arr[i])) or len(arr3[i]) != len(set(arr3[i])) or len(arr4[i]) != len(set(arr4[i])):
            list1.append(0)
        else:
            list1.append(1)

    if 0 in list1:
        print(f'#{_} 0')
    else:
        print(f'#{_} 1')

