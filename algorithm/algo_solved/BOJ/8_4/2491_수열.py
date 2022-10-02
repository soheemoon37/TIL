'''아놔 ㅋㅋㅋㅋㅋ 문제 대박이네
이거 처음에 for문 2번 돌렸음. 왜냐면 cnt 리셋을 못시키겠는거야
근데 메모리초과뜨고 시간초과뜸
여튼 구글링 한번했는데, for문 2번 안돌려도됨
else 이용해서 cnt 리셋할 수 있음
그리고 마지막에 틀렸다고 나오던데 maxV가 0으로 설정되면 안되고
1로 되있어야 함 그래야 길이 1인 경우에 값나옴'''

N = int(input())
arr = list(map(int, input().split()))

cnt = 1
maxV = 1
for i in range(N-1):
    if arr[i] <= arr[i+1]:
        cnt += 1
    else:
        cnt = 1
    if maxV < cnt:
        maxV = cnt

cnt = 1
for i in range(N-1):
    if arr[i] >= arr[i+1]:
        cnt += 1
    else:
        cnt = 1
    if maxV < cnt:
        maxV = cnt
print(maxV)

