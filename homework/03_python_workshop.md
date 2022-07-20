### 세로로 출력하기

자연수 number를 입력 받아, 1부터 number까지의 수를 세로로 한줄씩 출력하시오.

```python
num = int(input())

for i in range(1, num+1):
    print(i)
```



### 가로로 출력하기

자연수 number를 입력 받아, 1부터 number까지의 수를 가로로 한칸씩 띄어 출력하시오.

```python
num = int(input())

for i in range(1, num+1):
    print(i, end = ' ')
```



### 거꾸로 세로로 출력하기

자연수 number를 입력 받아, number부터 0까지의 수를 세로로 한줄씩 출력하시오.

```python
num = int(input())

for i in range(num, -1, -1):
    print(i)
```





### 거꾸로 출력해 보아요

자연수 number를 입력 받아, number부터 0까지의 수를 가로로 한칸씩 띄어 출력하시오.

```python
num = int(input())

for i in range(num, -1, -1):
    print(i, end = ' ')
```





### N줄 덧셈 (SWEA #2025)

입력으로 자연수 number가 주어질 때, 1부터 주어진 자연수 number까지를 모두 더한
값을 출력하시오. 단, 주어지는 숫자는 10000을 넘지 않는다. 예를 들어, 주어진 숫자가
10일 경우 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10 = 55이므로, 출력해야 할 값은 55이다.

```python
num = int(input())
a= list(range(1, num + 1))
print(sum(a))
```







### 삼각형 출력하기

자연수 number를 입력 받아, 아래와 같이 높이가 number인 삼각형을 출력하시오.

```python
num = int(input())
for i in range(1, num+1):
    print(' ' * (num-i)+'*' * i)
```





### 중간값 찾기

중간값은 통계 집단의 수치를 크기 순으로 배열 했을 때 전체의 중앙에 위치하는 수치를 뜻한다. 리스트 numbers에 입력된 숫자에서 중간값을 출력하라.

```python
numbers = [85, 72, 38, 80, 69, 65, 68, 96, 22, 49, 67,
51, 61, 63, 87, 66, 24, 80, 83, 71, 60, 64,
52, 90, 60, 49, 31, 23, 99, 94, 11, 25, 24]

numbers.sort()
print(numbers)

print(numbers[len(numbers)//2])
```


