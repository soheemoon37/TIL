T = int(input())

# 노드의 개수 V 와 리프 노드의 개수 M, 값을 출력할 노드 번호 L

for _ in range(1, T+1):
    print(f'#{_}', end=' ')
    V, M, L = map(int, input().split())
    tree = [0] * (V+1)  # tree 나무 저장할 리스트 만들기
    for i in range(M):
        idx, val = map(int, input().split())  # 입력받는 값을 트리에 추가
        tree[idx] = val
    for j in range(V-M, 0, -1):  # 리프노드를 제외하고 뒤에서부터 자식을 합한 값 채우기
        if j*2 <= V:  # 범위를 정해야함. 왼쪽자식만 있을수도있음.
            tree[j] = tree[j*2]
            if j*2+1 <= V:
                tree[j] += tree[j*2+1]
    print(tree[L])
