
T = int(input())
for _ in range(1, T+1):
    print(f'#{_}', end=' ')
    N, M = map(int, input().split()) # N:컨테이너수, M:트럭수
    list1 = list(map(int, input().split())) # 화물의 무게
    list2 = list(map(int, input().split())) # 트럭의 적재용량
    list1.sort(reverse=True) # 내림차순으로 정렬
    list2.sort(reverse=True)

    i = 0  # list1 의 인덱스값
    j = 0  # list2 의 인덱스값
    total = 0  # 총합 지금부터 구할거
    while True:
        if i == N or j == M:  # 인덱스가 각각 같아지면 멈춰야함. 아니면 인덱스에러뜸!!!!!
            break
        if list1[i] <= list2[j]:  # 트럭용량이 더 클때는 실을 수 있음
            total += list1[i]
            i += 1 # 실고 나서 인덱스 값 하나씩 올리기
            j += 1
        else: # 트럭용량이 더 적을 때는 list1에 있는거 하나 날리기(화물버림)
            i += 1
    print(total)
