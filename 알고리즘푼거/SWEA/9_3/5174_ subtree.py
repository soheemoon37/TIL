
T = int(input())

# 전위순회
def preorder(n):
    global cnt
    if n:
        cnt += 1   # 개수세기
        preorder(ch1[n])
        preorder(ch2[n])

for _ in range(1, T+1):
    print(f'#{_}', end=' ')
    E, N = map(int, input().split())
    V = E + 1
    arr = list(map(int, input().split()))
    # 자식리스트만들기
    ch1 = [0] * (V+1)
    ch2 = [0] * (V+1)
    for i in range(E):
        p, c = arr[i*2], arr[i*2+1]
        if ch1[p] == 0:  # 자식이 없으면 C 로 채우기
            ch1[p] = c
        else:  # 왼쪽 자식이 있으면 오른쪽에 C 채우기
            ch2[p] = c
    cnt = 0
    preorder(N)
    print(cnt)