# 스웨아 5204 문제로 푼건데 시간초과 뜸
# 근데 이게 병합정렬 코드임

def merge(left, right):
    global cnt
    rst = []
    if left[-1] > right[-1]:
        cnt += 1
    while len(left) > 0 or len(right) > 0:
        if len(left) > 0 and len(right) > 0:
            if left[0] <= right[0]:
                a = left.pop(0)
                rst.append(a)
            else:
                a = right.pop(0)
                rst.append(a)
        elif len(left) > 0:
            a = left.pop(0)
            rst.append(a)
        elif len(right) > 0:
            a = right.pop(0)
            rst.append(a)
    return rst


def merge_sort(M):
    global cnt
    if len(M) <= 1:
        return M
    left = []
    right = []
    c = len(M) // 2
    for x in M[0:c]:
        left.append(x)
    for x in M[c:len(M)]:
        right.append(x)
    left = merge_sort(left)
    right = merge_sort(right)
    return merge(left, right)

T = int(input())
for _ in range(1, T+1):
    print(f'#{_}', end=' ')
    N = int(input())
    M = list(map(int, input().split()))
    cnt = 0
    M1 = merge_sort(M)
    print(M1[N//2], end=' ')
    print(cnt)

