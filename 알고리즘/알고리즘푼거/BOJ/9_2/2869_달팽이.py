# 9/6. 실버5. 드디어 달팽이 문제풀었음
# 처음에 while이랑 for문 쓰다가 시간초과걸려서 구글링함
# 결국 그냥 수학문제였음

import math

# math 모듈에서 ceil 쓰면 올림해줌
''' 도달하는 일을 x일이라고 했을 때, 올라가는 횟수는 x번,
내려오는 횟수는 x-1번임
그래서 Ax - B(x-1) = V 가 되고 아래의 식임
이때, 정수로 나눠질수도 있지만 days 가 실수로 나오는 경우도있음
그래서 올림 해줘야 함'''

A, B, V = map(int, input().split())

days = (V - B) / (A - B)
print(math.ceil(days))