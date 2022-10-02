# 이거 그냥 큐 구현하는거고, 준봉이가 준 하나의 팁이 있음
# M만큼 도는게 N으로 나눈 나머지 만큼 도는 거라 B 로 정해둠

T = int(input())
for _ in range(1, T+1):
    N, M = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    B = M % N
    for i in range(B):
        a = arr.pop(0)
        arr.append(a)
    print(f'#{_} {arr[0]}')