import sys
sys.stdin = open("a.txt")

dict1 = {
    '0001101': '0',
    '0011001': '1',
    '0010011': '2',
    '0111101': '3',
    '0100011': '4',
    '0110001': '5',
    '0101111': '6',
    '0111011': '7',
    '0110111': '8',
    '0001011': '9'
    }
num = {
    '0': '0000', '1': '0001', '2': '0010', '3': '0011', '4': '0100', '5': '0101', '6': '0110', '7': '0111',
    '8': '1000', '9': '1001', 'A': '1010', 'B': '1011', 'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'
    }


T = int(input())
for _ in range(1, T+1):
    print(f"#{_}", end=' ')
    N, M = map(int, input().split())

    list1 = []
    for i in range(N):
        a = input()
        list1.append(a)

    list2 = []
    for i in list1:
        if i.count('0') != M:
            list2.append(i)
    list2 = list(set(list2))
    list3 = []
    for i in range(len(list2)):
        a = ''
        for j in range(len(list2[i])):
            a += num[list2[i][j]]
        list3.append(a)


    print(list3)
















