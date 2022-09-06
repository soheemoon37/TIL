# 최댓값 인덱스랑 최댓값 구하기
a = [1, 3, 4, 9, 5, 7]

max_idx = 0

for i in range(len(a)):
    if a[max_idx] < a[i]:
        max_idx = i
print(max_idx, a[max_idx])