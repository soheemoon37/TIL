# 윤년, 평년 구하기
year = int(input())

if (((year % 4) == 0) and ((year % 100 != 0))) or (year % 400 == 0):
    print(f'{year}년은 윤년입니다')
else:
    print(f'{year}년은 평년입니다')