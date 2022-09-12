### Authentication(인증)

- 신원 확인

- 사용자가 자신이 누구인지 확인하는것

### Authorization(권한, 허가)

- 권한 부여

- 인증된 사용자가 수행할 수 있는 작업을 결정

### User Model

- 로그인, 회원가입, 회원탈퇴, 회원정보수정 (CRUD)

### 왜 custom user model?

- 개발자들이 작성하는 일부 프로젝트에서는 django 에서 제공하는 built-in User model 의 기본 인증 요구사항이 적절하지 않을 수 있음

- django 는 현재 프로젝트에서 사용할 User Model 을 결정하는 AUTH_USER_MODEL 설정 값으로 Default User Model 을 재정의(override)할 수 있도록 함

### custom User model 로 대체하기

- 3단계 교재 그대로 따라하기

### 데이버베이스 초기화하기

- 0001,0002 지우기

- python manage.py makemigrations 하면 accounts 에도 migrations 가 생김

- python manage.py migrate 하기

- db 만들어진거 확인하기

- accounts.user 가 있을거임 원래는 auth.user 였대

- user 데이터들은 앞으로 accouts.user 에 등록됨

## 반드시 User 모델을 대체해야 할까?

- 대체하도록 강력하게 권장

- 커스텀 User 모델은 기본 User 모델과 동일하게 작동하면서도 필요한 경우 나중에 맞춤 설정할 수 있기 때문

- 단, User 모델 대체 작업은 프로젝트의 모든 migrations 혹은 첫 migrate 를 실행하기 전에 이 작업을 마쳐야함.

- **그냥 migrations 이랑 migrate 하기 전에 User 모델 대체하기**

### HTTP

- Hyper Text Transfer Protocol

- HTML 문서와 같은 리소스들을 가져올 수 있도록 해주는 프로토콜

- 요청(requests)과 응답(response)

- 특징
  
  - 비 연결 지향(connectionless) : 서버는 요청에 대한 응답을 보낸 후 연결을 끊음
  
  - 무상태(stateless) : 연결을 끊는 순간 클라이언트와 서버 간의 통신이 끝나며 상태 정보가 유지되지 않음, 클라이언트와 서버가 주고받는 메시지들은 서로 완전히 독립적

### 어떻게 로그인 상태를 유지할까?

- 그런데 우리가 로그인을 하고 웹 사이트를 사용할 때 페이지를 이동해도 로그인 "상태"가 유지됨

- 서버와 클라이언트 간 지속적인 상태 유지를 위해 "`쿠키와 세션`"이 존재

- 위에 HTTP 가 저런 속성들을 지니고 있는데, 그럼에도 불구하고 상태를 유지시켜주는거

- 예를 들어, 로그인이 한번 되어 있으면 유지되어야 하잖아. 그런거 유지시켜줌

### 쿠키(Cookie)

- HTTP 쿠키는 상태가 있는 세션을 만들도록 해 줌

- 요청을 보내면 응답 안에 쿠키가 들어있음. 사용자의 컴퓨터에 설치됨.

- 동일한 서버에 재요청 시 저장된 쿠키를 함께 전송

- 쿠키는 두 요청이 동일한 브라우저에서 들어왔는지 아닌지를 판단할 때 주로 사용됨.

- 이를 이용해 사용자의 로그인 상태를 유지할 수 있음

- 매 요청마다 로그인된 사용자라고 보내는 거임. 매 요청마다 받은 쿠키를 보내줘야함

### 쿠키 사용 목적

- 세션 관리
  
  - 로그인, 아이디 자동완성, 공지 하루 안 보기, 팝업 체크, 장바구니 등의 정보 관리

- 개인화
  
  - 사용자 선호, 테마 등의 설정

- 트래킹
  
  - 사용자 행동을 기록 및 분석

### 세션(Session)

- 사이트와 특정 브라우저 사이의 "state(상태)" 를 유지시키는 것

- 클라이언트가 서버에 접속하면 서버가 특정 session id 를 발급하고, 클라이언트는 session id 를 쿠키에 저장

- 클라이언트가 다시 동일한 서버에 접속하면 요청과 함께 쿠키(session id 가 저장된)를 서버에 전달

- 쿠키는 요청 때마다 서버에 함께 전송되므로 서버에서 session id 를 확인해 알맞은 로직을 처리

- session id 는 세션을 구별하기 위해 필요하며, 쿠키에는 session id 만 저장

### 쿠키 Lifetime(수명)

- Session cookie
  
  - 현재 세션(current session)이 종료되면 삭제됨
  
  - 브라우저 종료와 함께 세션이 삭제됨

### Session in Django p.52

- Django는 database-backed sessions 저장 방식을 기본 값으로 사용
  
  - session 정보는 Django DB 의 django_session 테이블에 저장
  
  - 설정을 통해 다른 저장방식으로 변경 가능

- Django 는 특정 session id 를 포함하는 쿠키를 사용해서 각각의 브라우저와 사이트가 연결된 session 을 알아냄

- 브라우저에 key 만 보내는거래

# Authentication in Web requests

### Login

- 로그인은 Session 을 Create 하는 과정

- 장고에서 `python manage.py createsuperuser` 입력

- username 에 admin 입력

### AuthenticationForm

- 로그인을 위한 built-in form
  
  - 로그인 하고자 하는 사용자 정보를 입력받음
  
  - 기본적으로 username과 password를 받아 데이터가 유효한지 검증

- request 를 첫번째 인자로 취함

### 

### 로그인 페이지 작성

- p. 59 따라서 입력하기

- accounts 에 templates 폴더 만들고 또 account 폴더 만들기

- login.html 파일 만들기

- runserver 해보면 로그인 페이지 나오는데 내가 직접 작성한게 아니고 저게 AuthenticationForm 인거래

- 빌트인 내장 form 인가봄

### 로그인 로직 작성

- 로그인 페이지 작성

- view 함수 login 과의 충돌을 방지하기 위해 import한 login 함수 이름을 auth_login 으로 변경해서 사용

### get_user()

- AuthenticationForm 의 인스턴스 메서드

- 유효성 검사를 통과했을 경우 로그인 한 사용자 객체를 반환

### 로그인 링크작성

- base.html 에 작성 p.65

### 현재 로그인 되어있는 유저 정보 출력하기 p.68

### Logout p.75

- 로그아웃은 Session 을 Delete 하는 과정

- 다음 2가지 일 처리함
  
  - 현재 요청에 대한 session data 를 DB 에서 삭제
  
  - 클라이언트의 쿠키에서도  sessionid 를 삭제
  
  - 둘 다 삭제한다고 알아두면 됨.

### 로그아웃 로직 작성하기 p.76

# Authentication with User

### 개요

- User Object 와 User CRUD 에 대한 이해
  
  - 회원가입, 회원탈퇴, 회원정보수정, 비밀번호 변경

### 회원가입

- 회원가입은 User 를 Create 하는 것이며 `UserCreationForm` built-in form 을 사용

- `UserCreationForm`
  
  - 주어진 username 과 password 로 권한이 없는 새 user 를 생성하는 ModelForm
  
  - 3개의 필드를 가짐
    
    - username (from the user model)
    
    - password1
    
    - password2

### 회원가입 페이지 작성 p.84

- login.html 에서 복붙해와서 조금만 바꾸면됨

- 한글로 페이지 내용 보고 싶으면 settings.py 에서 랭귀지를 'ko-kr' 로 바꾸기

- runserver 해보면 이게 바로 `UserCreationForm` 임

- base 템플릿에서 회원가입으로 이동하는 url 만들기

- 나머지 회원가입 로직 작성 해줘야함. view.py 에서

- 회원가입 진행 후 에러 페이지 확인(정상임)
  
  - 회원가입에 사용되는 UserCreationForm 이 우리가 대체한 커스텀 유저 모델이 아닌 기존 유저 모델로 인해 작성된 클래스이기 때문
  
  - UserCreationForm 이거를 상속받고 오버라이딩 하기 p.92 부터 코드구현

### 

### 커스텀 유저 모델을 사용하려면 다시 작성하거나 확장해야 하는 forms

- UserCreationForm, UserChangeForm

- 두 form 모두 class Meta: model = User 가 등록된 form 이기 때문에 반드시 커스텀(확장)해야 함 p.92

### 회원가입할 때 이메일 이런거 입력하게 하려면? 더 받고 싶은 필드가 있을 때

- class CustomUserCreationForm 에 이메일 필드 추가하기. 영상 다시 보셈

- 근데 이메일 처럼 있는 필드를 써야지 유저가 가지고 있지 않은 존재하지 않는 필드를 쓰는 건 안됨. 0001에 필드 있는거 나와있음. 아니면 django user object 구글링 하면 알수 있음.

- ```python
  accounts/forms.py
  class CustomUserCreationForm(UserCreationForm):
      class Meta(UserCreationForm.Meta):
          model = get_user_model()
          fields = UserCreationForm.Meta.fields + ('email',)
  ```

### get_user_model()

- "현재 프로젝트에서 활성화된 사용자 모델"을 반환

- 직접 참조하지 않는 이유
  
  - 예를 들어 기존 User  모델이 아닌 User 모델을 커스텀한 상황에서는 커스텀 User 모델을 자동으로 반환해주기 때문

- django 는 User 클래스를 직접 참조하는 대신 get_user_model() 을 사용해 참조해야 한다고 강조하고 있음.

### 근데 보통 회원가입하면 자동으로 로그인한 채로 화면 뜨지 않음? 그렇게 하려면?

- ```python
  accounts/views.py
  
  def signup(request):
      if request.method == 'POST':
          form = CustomUserCreationForm(request.POST)
          if form.is_valid():
              user = form.save()
              # 회원가입 후 바로 로그인되게 만들기
              auth_login(request, user)
              return redirect('articles:index')
  ```

### 회원탈퇴

- 회원 탈퇴하는 것은 DB에서 유저를 Delete 하는 것과 같음

- 회원탈퇴 로직작성 p.100
