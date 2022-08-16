import sys

sys.stdin = open("1216_회문2.txt")

# 와 내가 이거를 풀어버림 ㅠㅠㅠ 눈물 ㅠㅠㅠ
# 일단 열의 순환도 arr3로 나타내서 각각에서 가장 긴 값을 찾아야함
# 이게 아이디어를 for문 3개를 이용해서 구현해야 하는데
# 저기 k의 범위에서 100-j+1인데 처음에 100-j만 해놔서 답이 하나 틀렸었음
# 2부터 정한 이유는 문자를 2개부터 회문인지를 비교하는 거라 그렇게 한거.
# 어쨌든 길이 다 한 곳에 모으고 제일 큰 값 찾으면 됨.

for _ in range(1, 11):
    N = int(input())
    arr = [list(input()) for _ in range(100)]
    arr3 = []
    for j in range(100):
        arr2 = []
        for i in range(100):
            arr2.append(arr[i][j])
        arr3.append(arr2)
    arr4 = []
    for i in range(100):
        for j in range(100):
            for k in range(100-j, 1, -1):
                if arr[i][j:j+k] == arr[i][j:j+k][::-1]:
                    arr4.append(len(arr[i][j:j+k]))
    for i in range(100):
        for j in range(100):
            for k in range(100-j, 1, -1):
                if arr3[i][j:j+k] == arr3[i][j:j+k][::-1]:
                    arr4.append(len(arr3[i][j:j+k]))
    print(f'#{_} {max(arr4)}')



