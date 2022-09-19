'''구글링함.. 일단 이게 2, 3, 5, 7 로 나눠지면 소수가 아니잖아
그러고 나서 보면 i 의 제곱근도 i 의 약수니까 이거도 체크를 해줘야함
이상한게 range(2, int(i ** 0.5)+2) 로 범위를 만들었는데
틀렸습니다가 나옴... 뭐지...
여튼 제곱근까지 봐주면 되는듯?
막 여러방법 써보는데 답이 잘안나옴 ㅠㅠ'''

a, b = map(int, input().split())


for i in range(a, b+1):
    if i == 1:
        continue
    for j in range(2, int(i ** 0.5)+1):
        if i % j == 0:
            break
    else:
        print(i)