# 조합으로 풀었음,, 시간초과 날 줄 알았는데 안 났음

def nCr(n, r, s):
    if r == 0:
        if sum(comb) == 100:
            comb.reverse()
            for i in range(7):
                print(comb[i])
            return
    else:
        for i in range(s, n-r+1):
            comb[r-1] = A[i]
            nCr(n, r-1, i+1)


A = []
for i in range(9):
    a = int(input())
    A.append(a)

n = len(A)
r = 7
comb = [0] * r
nCr(n, r, 0)