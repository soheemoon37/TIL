# 전위순회
def preorder(n):
    global cnt
    if n:
        cnt = n
        print(n, end=' ')  # visit(n)
        preorder(ch1[n])
        preorder(ch2[n])
        

# 중위순회
def inorder(n):
    if n:
        inorder(ch1[n])        
        print(n, end=' ')
        inorder(ch2[n])
        

# 후위순회
def postorder(n):
    if n:
        postorder(ch1[n])
        postorder(ch2[n])
        print(n, end=' ')
        

# root 를 찾아보자
def find_root(V):
    for i in range(1, V+1):
        if par[i] == 0:
            return i



V = int(input())
arr = list(map(int, input().split()))
E = V - 1

# 부모를 인덱스로 자식 번호 저장
ch1 = [0] * (V+1)
ch2 = [0] * (V+1)
# 자식을 인덱스로 부모 번호 저장
par = [0] * (V+1)

for i in range(E):
    p, c = arr[i*2], arr[i*2+1]
    if ch1[p] == 0:  # 부모가 없으면 root
        ch1[p] = c
    else:
        ch2[p] = c
    par[c] = p

root = find_root(V)
# print(root)
# 3을 루트로 하는 서브트리에 속한 정점의 개수는?
# 자손의 개수는 위에 꺼 빼기 1 하면됨.
# 만약에 마지막 정점 물어보면? cnt 만든김에 cnt = n 으로 하면 마지막 정점 남아있음
cnt = 0
preorder(root)
print()
print(cnt)
# inorder(3)
# print()
# postorder(3)
# print()

# 입력
# 13
# 1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13