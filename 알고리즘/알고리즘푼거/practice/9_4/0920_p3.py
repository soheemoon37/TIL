dict1 = {'001101': '0',
         '010011': '1',
         '111011': '2',
         '110001': '3',
         '100011': '4',
         '110111': '5',
         '001011': '6',
         '111101': '7',
         '011001': '8',
         '101111': '9'}

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
    list2 = list(output)

    list3 = []
    i = 0
    while i < len(list2):
        if ''.join(list2[i:i+6]) not in dict1:
            i += 1
        else:
            list3.append(''.join(list2[i:i+6]))
            i += 6

    for i in list3:
        print(dict1[i], end=' ')
    print()
