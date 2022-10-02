def enq(n):
    global last
    last += 1       # 1번. 마지막 정점 추가하기
    heap[last] = n  # 마지막 정점에 key 추가
    c = last
    p = c // 2      # 완전이진트리에서 부모 정점 번호
    # 부모가 있고 부모 > 자식 인 경우 자리 교환(부모가 없거나 부모 < 자식 조건을 만족할 때까지)
    while p and heap[p] > heap[c]:
        heap[p], heap[c] = heap[c], heap[p]
        # 자식이 더 크면 계속 바꿔야 되니까 c, p 값 바꿔줌
        c = p
        p = c // 2


T = int(input())
for _ in range(1, T+1):
    print(f'#{_}', end=' ')
    V = int(input())
    arr = list(map(int, input().split()))
    heap = [0] * (V+1)
    last = 0
    for i in arr:
        enq(i)
    total = 0        # 마지막 노드의 조상노드들 값 더해주기
    while True:
        if V == 1:
            break
        if V // 2:
            total += heap[V//2]
            V = V // 2
    print(total)
