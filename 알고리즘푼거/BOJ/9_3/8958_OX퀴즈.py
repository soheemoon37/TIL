# 브론즈2

N = int(input())
for i in range(N):
    arr = list(input())
    # print(arr)
    cnt = 0
    total = 0
    for i in range(len(arr)):
        if arr[i] == 'O':
            cnt += 1
            total += cnt
        else:
            cnt = 0
    print(total)
