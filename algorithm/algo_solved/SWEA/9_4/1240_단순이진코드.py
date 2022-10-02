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
        if i.count(0) != M:
            list2.append(i)
            break

    a = list2[0]
    list3 = list(a)

    x = 0
    for i in range(len(list3)-1, -1, -1):
        if list3[i] == '1':
            x = i
            break

    list3 = list3[x-55:x+1]

    list4 = []
    i = 0
    while i < len(list3):
        if ''.join(list3[i:i+7]) not in dict1:
            i += 1
        else:
            list4.append(''.join(list3[i:i+7]))
            i += 7

    list5 = []
    for i in list4:
        list5.append(dict1[i])

    total1 = 0
    total2 = 0
    for i in range(len(list5)):
        if (i+1) % 2 == 1:
            total1 += int(list5[i])
        else:
            total2 += int(list5[i])

    if (total1 * 3 + total2) % 10 == 0:
        print(total1+total2)
    else:
        print(0)
