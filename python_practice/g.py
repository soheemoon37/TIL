# 정중앙 문자 구하기

a = input()
def get_middle_char(a):
    if len(a) % 2 == 1:
        return a[len(a)//2]
    else:
        return a[len(a)//2-1 : len(a)//2+1]
   
print(get_middle_char(a))


