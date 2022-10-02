T = int(input())
for _ in range(1, T+1):
    list1 = list(input())
    for i in range(len(list1)):
        if list1[i] == 'A':
            list1[i] = '10'
        elif list1[i] == 'B':
            list1[i] = '11'
        elif list1[i] == 'C':
            list1[i] = '12'
        elif list1[i] == 'D':
            list1[i] = '13'
        elif list1[i] == 'E':
            list1[i] = '14'
        elif list1[i] == 'F':
            list1[i] = '15'
    output = ""
    for i in list1:
        for j in range(3, -1, -1):
            output += "1" if int(i) & (1 << j) else "0"

    a = list(output)
    a_list = []
    while a:
        b = ''
        for i in range(7):
            if a:
                c = a.pop(0)
                b += c
        a_list.append(b)

    for i in a_list:
        total = 0
        for j in range(len(i)):
            total += int(i[j]) * (2 ** (len(i)-1-j))
        print(total, end=' ')
    print()
