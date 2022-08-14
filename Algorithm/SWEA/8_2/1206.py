# SWEA 1206.
# 얖 옆에 2개씩은 일단 제외하고 자신의 위치가 i라고 한다면 양옆 +-2개씩 살펴보면됨
# 본인 제외하고 최대값인 거 찾아서 최대값이 자신보다 작은 경우에 얼마나 작은지 count하면 됨
# 되게 어려운 줄 알았는데 생각보다 쉬운 문제


for _ in range(1, 11):
    N = int(input())
    arr = list(map(int, input().split()))
    list1 = []
    for i in range(2, N-2):
        maxV = 0
        for c in range(i-2, i+3):
            if c != i:
                if arr[c] > maxV:
                    maxV = arr[c]
            cnt = 0
            if maxV < arr[i]:
                cnt += arr[i] - maxV
        list1.append(cnt)
    print(f'#{_} {sum(list1)}')