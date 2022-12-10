# 6 이랑 9 뒤집어서 사용하는 거만 주의하면 됨

list1 = [0] * 10

a = input()

for i in range(len(a)):
    list1[int(a[i])] += 1

if (list1[6] > (list1[9] + 1)) or (list1[9] > (list1[6] + 1)):
    if (list1[6] + list1[9]) % 2 == 0:
        list1[6], list1[9] = (list1[6] + list1[9]) // 2, (list1[6] + list1[9]) // 2
    else:
        list1[6], list1[9] = (list1[6] + list1[9]) // 2 + 1, (list1[6] + list1[9]) // 2 + 1

print(max(list1))


