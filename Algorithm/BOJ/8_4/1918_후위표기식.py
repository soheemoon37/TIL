arr = list(input())

sta = []

for i in arr:
    if 65 <= ord(i) <= 90:
        print(i, end='')
    else:
        if i == '(':
            sta.append(i)
        elif i == '*' or i == '/':
            while sta:
                if sta[-1] == '(' or sta[-1] == '+' or sta[-1] == '-':
                    break
                else:
                    print(sta.pop(), end='')
            sta.append(i)
        elif i == '+' or i == '-':
            while sta:
                if sta[-1] == '(':
                    break
                else:
                    print(sta.pop(), end='')
            sta.append(i)
        elif i == ')':
            while sta:
                if sta[-1] == '(':
                    sta.pop()
                    break
                else:
                    print(sta.pop(), end='')
if sta:
    for i in range(len(sta)-1, -1, -1):
        print(sta[i], end='')




