import sys

sys.stdin = open("4865_글자수.txt")

# 처음 입력값에 반복되는 거도 있길래 그거 지우려고 set이용함
# arr에 있는 각각에 대해서 arr2에 몇 개가 있는지 확인하고 빈 리스트에 채우기
# 그기서 최대값 구하면 끝

T = int(input())
for _ in range(1, T+1):
    arr = list(set(input()))
    arr2 = list(input())
    arr3 = []
    for i in range(len(arr)):
        arr3.append(arr2.count(arr[i]))
    print(f'#{_} {max(arr3)}')