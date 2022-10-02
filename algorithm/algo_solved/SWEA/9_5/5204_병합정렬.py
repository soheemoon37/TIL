
def merge_sort(arr):
    global cnt
    if len(arr) < 2:
        return arr

    mid = len(arr) // 2
    low_arr = merge_sort(arr[:mid])
    high_arr = merge_sort(arr[mid:])

    if low_arr[-1] > high_arr[-1]:
        cnt += 1

    merged_arr = []
    l = h = 0
    while l < len(low_arr) and h < len(high_arr):
        if low_arr[l] < high_arr[h]:
            merged_arr.append(low_arr[l])
            l += 1
        else:
            merged_arr.append(high_arr[h])
            h += 1
    merged_arr += low_arr[l:]
    merged_arr += high_arr[h:]
    return merged_arr

T = int(input())
for _ in range(1, T+1):
    print(f'#{_}', end=' ')
    N = int(input())
    M = list(map(int, input().split()))
    cnt = 0
    M1 = merge_sort(M)
    print(M1[N//2], end=' ')
    print(cnt)