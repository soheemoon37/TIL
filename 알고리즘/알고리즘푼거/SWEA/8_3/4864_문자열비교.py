import sys

sys.stdin = open("4864_문자열비교.txt")

# 일단은 for문 쓰기전에 범위 정해놓고, 슬라이스해서 arr2에 있는 부분이랑 arr이랑 같은지 확인
# for-else 문 썼음. if문에서 break 안되면 else로 넘어가고 그 다음 다시 돔.

T = int(input())

for _ in range(1, T+1):
    arr = input()
    arr2 = input()
    for i in range(len(arr2) - len(arr) + 1):
        if arr2[i:i+len(arr)] == arr:
            print(f'#{_} 1')
            break
    else:
        print(f'#{_} 0')
