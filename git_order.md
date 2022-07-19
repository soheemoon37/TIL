#### 미리 확인할 것

- 사용자 이름, 이메일 확인하는 법
  - git bash 터미널에 `git config --global --list` 입력
- 사용자 이름, 이메일 설정 안되어 있다면
  - git bash 터미널에 `git config --global user.name soheemoon37` 입력
  - git bash 터미널에 `git config --global user.email tnghgml37@gmail.com` 입력
- 이름, 이메일 재설정 후 다시  `git config --global --list` 로 확인

#### HWS 폴더 클론하기

1. lab.ssafy.com 로그인

2. Projects 문소희/HWS 클릭

3. clone 주소 복사

4. 바탕화면에서 git bash 열기

5. git bash 터미널에 `git clone <복사한 주소>` 입력

#### pull_only 폴더 클론하기

1. lab.ssafy.com 로그인

2. Projects ssafy 8기 / 부울경2반 / webex_lecture  클릭

3. clone 주소 복사

4. 바탕화면에서 git bash 열기

5. git bash 터미널에 `git clone <복사한 주소> pull_only` 입력

#### 작업하기

1. 위의 작업을 했으면 바탕화면에 hws폴더, pull_only 폴더가 있을거임

2. pull_only의 날짜별 폴더 복사하여 hws폴더에 붙여넣기

3. hws폴더에서 git bash 열기

4. git bash 터미널에 `jupyter notebook` 입력
   
   `작업 중에 git bash 터미널 닫지 말기`

5. 작업 다 한 후 git bash 터미널에서 `Ctrl + C` 입력

#### 푸쉬하기

1. hws폴더에서 git bash 열기
2. git bash 터미널에 `git status` 로 작업사항 확인
3. git bash 터미널에 `git add .` or `git add <filename>` 입력
4. git bash 터미널에 `git commit -m "0718 HWS 제출"` 입력
5. git bash 터미널에 `git push origin master` 입력
