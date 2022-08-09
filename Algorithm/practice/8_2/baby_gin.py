import sys

sys.stdin = open("baby_gin.txt")

T = int(input())

for test_case in range(1, T+1):
    count = [0] * 10
    arr = list(map(int, input()))
    run = 0
    triplet = 0
    # 카운팅 정렬 이용
    for i in range(6):
        count[arr[i]] += 1
    # triplet 일때 제거
    for c in range(10):
        if 3 <= count[c] < 6:
            count[c] -= 3
            triplet += 1
        elif count[c] == 6:
            count[c] -= 6
            triplet += 2
    # run 일때 제거
    for i in range(8):
        if count[i] == count[i+1] == count[i+2] == 1:
            count[i] -= 1
            count[i+1] -= 1
            count[i+2] -= 1
            run += 1
        elif count[i] == count[i+1] == count[i+2] == 2:
            count[i] -= 2
            count[i+1] -= 2
            count[i+2] -= 2
            run += 2
    # 각각의 경우를 대입하여 1 or 0 출력
    if (run == 2 and triplet == 0) or (run == 0 and triplet == 2) or (run ==1 and triplet == 1):
        print(f'#{test_case} 1')
    elif (run == 1 and triplet == 0) or (run == 0 and triplet == 1) or (run == 0 and triplet == 0):
        print(f'#{test_case} 0')
