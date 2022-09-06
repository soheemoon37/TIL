# 최댓값 구하기
a = [1, 9, 8, 5, 7, 48, 5, 2]

max_value = 0
for i in a:
    if max_value < i:
        max_value = i

print(max_value)