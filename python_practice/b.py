# map과 enumerate

str_nums = ['1000', '100', '1']

def double_numbers(x):
    return int(x) * 2

a = list(map(double_numbers, str_nums))
print(a)

b = list(enumerate(str_nums))
print(b)