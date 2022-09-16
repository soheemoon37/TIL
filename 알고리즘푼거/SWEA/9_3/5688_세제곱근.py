T = int(input())
for _ in range(1, T+1):
    print(f"#{_}", end=' ')
    N = int(input())
    X = int(N ** (1/3))  # 부동소수점 때문에 int 해줌
    ans = -1 # 안되면 -1 두려고 디폴트값설정
    for i in [X, X+1]: # 부동소수점때문에 X 가 1자리 적게나오니까 두 수 비교
        if i ** 3 == N: # 세제곱했을 때 N 이면 i 넣기
            ans = i
    print(ans)
