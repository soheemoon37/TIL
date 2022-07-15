### git

- 분산 버전 관리 프로그램
  - 변경사항을 기록하는 파일 `# 최종최종최종` `# 근데 수십억장짜리 코드`
  - 변경사항s + 최종만 남겨두기
  - 변경사항만 관리하는 게  git
  - 불나도 안전하게 살아있으니 살리면됨
  - `# 앞으로 싸피 깃에 과제 올라오면 다운받고 과제올리기`



### git hub

- `# 개발자 채용과정에서 git hub를 본당`



#### GUI와 CLI

- GUI(Graphic User Interface)
- CLI(Command Line Interface)
- cmd 명령 프롬프트 `# 예전엔 다 여기서 컴퓨터에 명령내림`
- `# CLI이 불편해서 >>> GUI`
- `# CLI로 git hub 배울거임.`



#### git bash

- 탐색기 - windows10 - 사용자 - SSAFY - 마우스오른쪽클릭 - git bash
- 디렉토리랑 폴더랑 비슷한 개념으로 보면 됨.
- `$` 상태에서 조작
- **touch**
  - `touch a.txt`
  - 파일생성
  - 띄어쓰기 구분해서 여러파일 생성 `touxh a.txt b.txt c.txt`

- **start .** `# 띄어쓰기포함`
  - 현재문서 띄어짐

- **mkdir** (make directory)

  - `mkdir folder_a`
  - 폴더생성

- **cd** (change directory)

  - `cd ..` : 상위폴더로
  - cd test : test 폴더로 바꿈

- **pwd** (print working directory)

  - 현재폴더띄어짐

- **ls** 

  - 현재파일뭐있는지

- **ls -l**

  - 파일 정보 더 자세히

- **mv** (move)

  - 같은 폴더 내에서  move  는 rename
  - 다른 폴더 내에서의  move가 진짜이동 
  - `mv s.txt ../test`

- **rm** (remove)

  - `rm q.txt` 복구안됨

- git bash로 만든 폴더에서  vs코드 열고 bash에서 여러 작업 수행

  

- ![image-20220715153839443](TIL_3.assets/image-20220715153839443.png)



#### 절대경로와 상대경로

- **절대경로** : 루트 디렉토리에서 목적 파일까지 모든 경로가 전부 포함
  - `C:/user/ssafy~
- **상대경로** : *현재 작업 중 디렉토리 기준*으로 계산
  - 나로부터의 거리 표시 기호
    - ./ : 현재폴더
    - ../ : 상위폴더(부모폴더)
    - 폴더다르면 ../kbk/k.txt `# 일단 상위폴더로 가서 폴더바꾸고 파일이름적기`



### 다시 git

git init  내가 추적할 파일

보통 working directory 이거임

아직 추적 시작안한거는 untracked file이라 함

`# 반드시   git   쓰고 명령 쓰기`

git add NY_project.txt 이제 추적할 파일이라 이거는

Staging Area에 옮겨짐

untracked file은 없어진거.

이제 뉴욕파일은 Staging Area 여기 있음 

git commit : 추적하고 있었는데 확정짓겠다 #도장꽝

여기다가 message적을 수 있음



#### vs코드에 활용

git init 적고 문서 보기에 숨긴항목 체크하면 git 생겨있음

셋업하기

`git config --global user.name soheemoon37`

`git config --global user.email tnghgml37@gamil.com`

확인해보기

`git config --global --list`

U가 생겨있음

`git status` : 현재 상태 확인

`git add ny_project.txt`

ny_project는 A로 변해있음

`git rm --cached ny_project.txt`

다시 U로 변함

변경사항 적고

`git add ny_project.txt`

다시 A로 변함

`git commit -m "1st commit"`

또 변경사항 적기

`git add ny_project.txt`

`git log`

`git commit -m "2nd commit"`

`git log` 2가지 나타남

이상하게 뜨면 `:wq ` 쳐보셈



#### git hub 이용

깃허브에 보낼때는 push

깃허브에서 가져올 때 처음에만 clone

그 다음부터는 pull

파일 보낼 때 다리가 필요하잖슴. `git remote add` 이용

`git remote add origin https://github.com/soheemoon37/test.git`

연결하고 `git remote -v` 이걸로 확인

마지막으로 보내기

`git push -u origin master`