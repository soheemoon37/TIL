# 윤년, 평년 구하기
num = int(input())

if num % 4 == 0:
    if num % 100 == 0:
        if num % 400 == 0:
            print('윤년')
        else:
            print('평년')
    else:
        print('윤년')
else:
    print('평년')