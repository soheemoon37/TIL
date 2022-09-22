
'''arr 의 1 번째 인덱스를 기준으로 오름차순으로 정렬해야함!
[[1, 5], [2, 3], [3, 4]] 가 반례임. 0번 인덱스를 기준으로 정렬했을 때
종료시간이 5라서 뒤에 2개는 포함이 안 됨'''

T = int(input())
for _ in range(1, T+1):
    print(f'#{_}', end=' ')
    N = int(input())
    arr = [list(map(int, input().split())) for i in range(N)]
    arr.sort(key=lambda x:x[1])
    a = [arr[0]]   # 정렬한 후에 arr 의 맨 앞에 값 저장해놓기. 가장 빨리 종료된 거임
    for i in range(1, N):
        if a[-1][1] <= arr[i][0]: # 시간 안 어긋나는 거는 a 에 저장. 그리고 a랑 arr 비교하는거임
            a.append(arr[i])
        else:
            continue
    print(len(a))
