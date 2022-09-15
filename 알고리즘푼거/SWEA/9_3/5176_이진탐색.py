import sys
sys.stdin = open("b.txt")

# 1231_중위순회 참고

def inorder(n):
    global cnt
    if n <= V:
        inorder(2 * n)
        tree[n] = cnt
        cnt += 1
        inorder(2 * n + 1)

T = int(input())
for _ in range(1, T+1):
    print(f'#{_}', end=' ')
    V = int(input())
    tree = [0] * (V+1)
    cnt = 1
    inorder(1)
    print(tree[1], end=' ')
    print(tree[V//2])