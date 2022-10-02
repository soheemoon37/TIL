# 부분집합 만들기

# 비트연산이용

arr = [3, 6, 7, 1, 5, 4]
n = len(arr)


for i in range(1, 1<<n):  # 공집합 빼려면 1부터 시작
    for j in range(n):
        if i & (1<<j):  # j 의 비트가 0이 아니면 arr[j] 부분집합의 원소
            print(arr[j], end=' ')
    print()


# 재귀이용

def f(i, k):
    if i == k:
        # print(bit)
        for j in range(k):
            if bit[j]:
                print(arr[j], end=' ')
        print()
    else:
        bit[i] = 0
        f(i+1, k)
        bit[i] = 1
        f(i+1, k)

arr = [3, 6, 7]
n = len(arr)

bit = [0] * n
f(0, n)