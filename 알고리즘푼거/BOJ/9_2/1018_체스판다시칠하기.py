# 1018. 체스판 다시 칠하기
# 220910. 실버4. 몽실도움

n, m = map(int, input().split())
A = []
mini = 64

for i in range(n):
    A.append(input())

for a in range(n-7):
    for b in range(m-7):
        w_index = 0
        b_index = 0
        for c in range(8):
            for d in range(8):
                # 왼쪽 위가 W 일때
                if (c+d)%2 == 0: 
                    if A[a+c][b+d] != 'W':
                        w_index += 1
                else:
                    if A[a+c][b+d] != 'B':
                        w_index += 1
                # 왼쪽 위가 B 일때
                if (c+d)%2 == 0: 
                    if A[a+c][b+d] != 'B':
                        b_index += 1
                else:
                    if A[a+c][b+d] != 'W':
                        b_index += 1
        mini = min(mini, w_index, b_index)
print(mini)
