import sys
input = sys.stdin.readline

N = list(input())
sta = [N[0]]
for i in range(1, len(N)):
    if N[i] != sta[-1]:
        sta.append(N[i])
    else:
        continue
a = sta.count('0')
b = sta.count('1')

print(min(a,b))