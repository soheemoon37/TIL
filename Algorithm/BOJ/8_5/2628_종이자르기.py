W, H = map(int, input().split())
N = int(input())
H_list = []
W_list = []
for i in range(N):
    a = list(map(int, input().split()))
    if a[0] == 0:
        H_list.append(a)
    else:
        W_list.append(a)
H_list.append([0, H])
H_list.insert(0, [0, 0])
W_list.append([1, W])
W_list.insert(0, [1, 0])
H_list.sort(key= lambda x:x[1])
W_list.sort(key= lambda x:x[1])

maxH = 0
for i in range(len(H_list)-1):
    if H_list[i+1][1] - H_list[i][1] > maxH:
        maxH = H_list[i+1][1] - H_list[i][1]
maxW = 0
for i in range(len(W_list)-1):
    if W_list[i+1][1] - W_list[i][1] > maxW:
        maxW = W_list[i+1][1] - W_list[i][1]
print(maxH * maxW)
