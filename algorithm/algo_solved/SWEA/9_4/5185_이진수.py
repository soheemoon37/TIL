T = int(input())
for _ in range(1, T+1):
    print(f"#{_}", end=' ')
    a, b = input().split()
    list1 = list(b)
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
    print(output)
