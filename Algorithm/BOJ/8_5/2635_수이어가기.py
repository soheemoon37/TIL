N = int(input())

max_list = []
len_max = 0

for i in range(1, N+1):
    arr = [N, i]
    while True:
        a = arr[-2] - arr[-1]
        if a >= 0:
            arr.append(a)
        else:
            break
    if len(arr) > len_max:
        len_max = len(arr)
        max_list = arr
print(len_max)
for i in range(len_max):
    print(max_list[i], end=' ')