# 수의 평균 구하기

arr = [1, 3, 4, 5, 4, 4, 7, 9]

total = 0
count = 0


for num in arr:
    total += num
    count += 1


print(total / count)
print(sum(arr) / len(arr))


for i in range(len(arr)):
    total += arr[i]
    count += 1
