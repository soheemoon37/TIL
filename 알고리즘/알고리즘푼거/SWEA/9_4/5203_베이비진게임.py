T = int(input())
for _ in range(1, T+1):
    print(f'#{_}', end=' ')
    arr = list(map(int, input().split()))
    arr1 = []
    arr2 = []
    for i in range(12):  # 각각 받은 숫자카드 나누기
        if i % 2 == 0:
            arr1.append(arr[i])
        else:
            arr2.append(arr[i])

    check = True  # 이거 설정해서 되풀이?안되도록 만들기
    for i in range(3, 7): # 숫자카드 개수가 3~6 일 때 확인해야함. 3~6 일 때 각각 확인할거임.
        if not check:  # 이 코드 안 넣으니까 테스트 케이스 몇개 안맞음. check 가 False 일 때는 그냥 break 해야함
            break
        count1 = [0] * 10 # 카운팅 정렬 사용
        count2 = [0] * 10
        for j in range(len(arr1[:i])):  # 슬라이스해서 일단 카운팅하기
            count1[arr1[j]] += 1
        for k in range(len(arr2[:i])):
            count2[arr2[k]] += 1

        for c in range(10): # 먼저 player 1 카드 확인/ 트리플릿이나 런이 되면 바로 1 출력하고 check 바꾸기
            if count1[c] >= 3:
                print(1)
                check = False
                break
            if c <= 7:
                if count1[c] >= 1 and count1[c+1] >= 1 and count1[c+2] >= 1:
                    print(1)
                    check = False
                    break

        if check: # player 1에서 안 끝나고 넘어오는거니까 check=True 일 때만 넘어가기
            for c in range(10):  # player 1 이랑 똑같은 코드. 트리플릿이나 런 되면 2 출력하고, check=False 로 바꾸기
                if count2[c] >= 3:
                    print(2)
                    check = False
                    break
                if c <= 7:
                    if count2[c] >= 1 and count2[c+1] >= 1 and count2[c+2] >= 1:
                        print(2)
                        check = False
                        break

    else: # 다 돌고 check=True 이면 무승부라서 0 출력
        if check:
            print(0)
