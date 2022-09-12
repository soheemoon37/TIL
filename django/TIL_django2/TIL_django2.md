# :cloud:Django 0830

## :sparkles:index

### 1. Namespace

### 2. Django Model

### 3. Queryset API

### 4. CRUD with view functions

### 5. Admin site

# Namespace

- 개체를 구분할 수 있는 범위를 나타내는 namespace(이름 공간)에 대한 이해

- 앱들이 여러 개 있을 때, 페이지의 이름이 겹칠 때 문제가 발생함

- URL namespace 를 사용하면 서로 다른 앱에서 동일한 URL 이름을 사용하는 경우에도 이름이 지정된 URL 을 고유하게 사용할 수 있음

- 앱네임 적고, 각각의 앱에 `urls.py` 생성 **p.9**

- 앞으로 url tag 에 앞에 앱이름 적어야 함.

- **app_name 을 지정한 이후에는 url 태그에서 반드시 app_name:url_name 형태로만 사용해야함. 그렇지 않으면 NoReverceMatch 에러가 발생**

- `templates 에 앱이름과 같은 폴더 만들기` **중요!!!!!

- 폴더 구조 변경 후 변경된 경로로 해당하는 모든 부분을 수정하기 **p.17**

- 반드시 Template namespace 를 고려해야할까?
  
  - 만약 단일 앱으로만 이루어진 프로젝트라면 상관없음
  
  - 여러 앱이 되었을 떄에도 템플릿 파일 이름이 겹치지 않게 하면 되지만, 앱이 많아지면 대부분은 같은 이름의 템플릿 파일이 존재하기 마련

# Django Model

- Model 의 핵심 개념과 ORM 을 통한 데이터베이스 조작 이해

- Django 는 웹 애플리케이션의 데이터를 구조화하고 조작하기 위한 추상적인 계층(모델)을 제공

### database

- 체계화된 데이터의 모임

- 검색 및 구조화 같은 작업을 보다 쉽게 하기 위해 조직화된 데이터를 수집하는 저장 시스템

- database 기본구조
  
  - 스키마(schema)
  
  - 테이블(Table)
  
  - 
