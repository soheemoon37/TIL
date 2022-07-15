### 중요한 사안들

- 공용설치문서

[싸피문서설치사이트](https://abit.ly/ssafy8-document)

- 텔레그램, 디스코드, 깃 설치 `하...`





### 본격 파이썬 공부

- string  글자
- 숫자에 ' '를 붙이면 문자가 된다
- 58 숫자, '58' 글자
- assignment 할당기호
- 리스트 [] 사용

- 딕셔너리{}

  - 이름표를 단 여러 개의 값을 저장할 수 있는 저장공간

  - ex) {"영등포구" : "58"}

  - 이 때, "영등포구"는 key, "58"는 value

- range(start, end, step)
  - step  은 증가칸수

- abs( ) 절댓값
- len('hi') = 2, len(['hi']) = 1







### 본격 파이썬 공부2

- 모듈(.py)

  - 함수나 변수 등을 모아 놓은 파이썬 파일

  - 다른 모듈꺼 쓸 때,   import 이용.

  - ``` python
    import phone_book
    print(phone_book.menu) # 소속밝히기
    ```



- `random 모듈`

- ```python
  import random
  
  menu = ['뚝불', '삼계탕', '수육']
  pick = random.choice(menu)
  print(pick)
  ```



- `random.sample`

  - 여러 개 중에 중복 안 되게 뽑기 ex)로또

  - 로또번호뽑기

  - ```python
    numbers = list(range(1, 46))
    # print(numbers)
    
    import random
    lucky = random.sample(numbers, 6)
    print(lucky)
    ```



- 두 list 같은지 비교하기

- ```python
  a = [1, 3, 4, 6]
  b = [4, 6, 3, 1]  # sort를 이용해야 순서 정리해서 같은지 확인할 수 있음
                    # 그게 아니라면 다음과 같은 방법 이용
  member = 0
  for i in range(4):
      if b[i] in a:
          member += 1
  if member == 4:
      print('same')
  else:
      print('not same')
  ```



- 랜덤번호가 실제로또번호와 같을수 있는지 여러번 확인하기

- ```python
  numbers = list(range(1, 46))
  
  import random
  
  winner = [10, 14, 16, 18, 29, 35]
  
  for chance in range(10): # range(num)에서 num은 원하는 확인수만큼 입력
      lucky = random.sample(numbers, 6)
      member = 0
      for i in range(6):
          if lucky[i] in winner:
              member += 1
      if member == 6:
          print('same')
      else:
          print('not same')
  ```



### 본격 파이썬 공부3

- [이름 입력하면 예상나이 알려주는 사이트](https://agify.io/)

- `json viewer` : 코딩 소스 알기쉽게 볼수있도록 변환해주는 프로그램([구글](https://google.com)에서 다운받기)

- **pip install requests**를 터미널에 적은후

  - ```python
    import requests
    url = 'https://api.agify.io/?name=moon'
    print(requests.get(url).json())
    ```



`# 나 정리 꽤 잘한 거 같음`

