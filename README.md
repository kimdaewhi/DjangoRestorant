# Django For Ubuntu 환경 세팅
⭐ https://www.codeit.kr/community/questions/UXVlc3Rpb246NjJlYTg5ZmNjN2FiMjgzYjFkYmZlMGFj

## 👍 Tips!!
1. **로컬 디바이스에 있는 파일을 ubuntu 디렉토리에 가져오는법**
  - ubuntu의 원하는 폴더 디렉토리로 이동
  - `explorer.exe .` 명령어 입력

 ```c#
 /* WSL(Windows Subsystem for Linux)이란? */
 ⭐ Windows 운영 체제에서 Linux 바이너리 및 명령을 실행할 수 있는
    Windows의 기능(하위 시스템), 즉, 리눅스 호환 환경임.
    
 ```

 ### 1. WSL2 업데이트 프로그램 설치

 ### 2. **Windows 기능 켜기/끄기**
- Linux용 Windows 하위 시스템
- Windows 하이퍼바이저 플랫폼
- 가상 머신 플랫폼

### 3. **BIOS에서 Intel VMX 활성화**

### 4. **MS Store에서 Ubuntu LTS 설치**
  * ⭐**LTS란?**  
    Long Term Support, 즉 장기지원을 의미.

### 5. Ubuntu 가상환경 실행(관리자 모드)

### 6. Ubuntu 환경세팅
   ```c
   // [1] Ubuntu 환경 업데이트
   sudo apt-get update

   // [2] 개발에 필요한 패키지 설치
   sudo apt-get install -y make build-essential \
   libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev \
   wget curl llvm libncurses5-dev libncursesw5-dev \
   xz-utils tk-dev git python-pip sqlite3

   // [3] 디렉토리 생성 및 vscode 실행
   mkdir [디렉토리 명]
   cd [디렉토리 명]

   code .
   ```
   ✏️설정 완료 후 vscode 실행, WSL-Remote 라이브러리 설치

### 7. pyenv, pyenv-virtualenv 설치 및 세팅
  ```python
  curl https://pyenv.run | bash

  # bash SHELL 사용 여부 확인
  echo $SHELL


  # case 1. bash Shell
  sed -Ei -e '/^([^#]|$)/ {a \
  export PYENV_ROOT="$HOME/.pyenv"
  a \
  export PATH="$PYENV_ROOT/bin:$PATH"
  a \
  ' -e ':a' -e '$!{n;ba};}' ~/.profile

  echo 'eval "$(pyenv init --path)"' >>~/.profile
  echo 'eval "$(pyenv init -)"' >> ~/.bashrc
  echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.bashrc


  # case 2. zsh Shell
  echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.zprofile
  echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.zprofile
  echo 'eval "$(pyenv init --path)"' >> ~/.zprofile
  
  echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.profile
  echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.profile
  echo 'eval "$(pyenv init --path)"' >> ~/.profile
  
  echo 'eval "$(pyenv init -)"' >> ~/.zshrc
  echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.zshrc


  # python 설치
  pyenv install [version]


  # python 가상환경 설정
  pyenv virtualenv 3.7.13 django-envs
  # 설치된 리스트를 확인해보면 다음과 같이 나온다.
  #  3.7.13
  #  3.7.13/envs/django-envs
  #  3.8.13
  #  django-envs --> /home/kimdaewhi/.pyenv/versions/3.7.13/envs/django-envs 
  #  ⬆️ 이건 바로가기와 동일하다~!


  # global 가상환경 적용
  pyenv global 3.8.13

  # local 폴더로 이동해서 local 가상환경 적용
  pyenv local django-envs
  ```


### 8. django 설치 및 project, app 생성
  ```
  pip3 install django==[version]
  django-admin startproject [프로젝트명]
  django-admin startapp [App명]
  ```

### 9. 생성한 django app 연결
  - settings.py >> INSTALLED_APPS에 생성한 app 추가


## 템플릿 언어
템플릿 작성 시 편의성 제공
  - **템플릿 변수** 
    view에서 전달받은 변수를 `{{ }}` 를 이용해서 사용 가능. 속성 `.` 연산자 사용 가능  
    (ex) `user = {"name" : "우재", "coffee" : True}`

  - **템플릿 필터**
    템플릿 변수에 파이프 ` | ` 를 쓰고 템플릿 필터를 사용하면 템플릿 변수를 특정 형식으로 변환 가능  
    default, capfirst, random, upper & lower 등 다양한 연산자 지원.
    (ex) `{{ variable|filter:args }}`

  - **템플릿 태그**
    템플릿을 작성할 때 반복문, 조건문 등의 로직 등 프로그래밍 문법 지원 `{% tag %}`로 사용 가능  
    (ex) `{% tag %} ~ {% endtag %}`

  - **템플릿 주석**  
    `{# #}` 태그 사용하여 주석 기능 제공


## 템플릿 상속
  - bock, extends



## Elegant URL
  - 동적 url  
    ex) `path('menu/<str:food>/', views.food_detail)`  
    menu/food를 문자열로 인식.  
    food_detail 호출 시 food에 대한 값을 parameter로 전달.
    전달한 parameter를 토대로 context 생성 및 템플릿 변수 사용하여 웹페이지 출력.


## Model
  - makemigrations
  - migrate
  - showmigrations
  - sqlmigrate [객체명] [번호]

  - python manage.py shell : 사용자 명령어 받아서 해석, 프로그램 실행
  ```
  from foods.models import Menu



  Menu.objects.create (name="가라아게",
                      desc="튀김이 얇고 바삭한 일본식 닭튀김",
                      price=14000,
                      img="foods/images/karaage.jpg" )
  ```  


### Django ORM 문법
  ``` 
    Menu.objects.all().values()
    Menu.objects.all().values('{컬럼명}')
    Menu.objects.order_by('{-}컬럼')

    ✏️ 데이터 조회
    Menu.objects.filter(name__contains="코") >> "코" 라는 단어가 들어간 DataSet 조회
    Menu.objects.filter(price__range=(2000,10000))  >> price 컬럼이 2000 ~ 10000 사이에 해당하는 DataSet
    ⭐⭐ filter 대신 get 함수를 사용하면 단일 데이터 조회. 조회 결과가 2개 이상이면 에러 발생
    
    ✏️ 데이터 수정/삭제
    ** 수정
    data = Menu.objects.get(id={ID})
    data.[필드] = "변경 필드 값"
    data.save()

    ** 삭제
    data = Menu.objects.get(id={ID})
    data.delete()
  ```

### QuerySet
  DB에서 데이터를 조회, 필터링 및 가공하기 위한 객체입니다. QuerySet은 Django ORM을 통해 데이터베이스에 대한 쿼리를 실행하고 결과를 Python 객체로 반환


## 관리자 도구 사용
**1. 관리자 계정 생성** : python manage.py createsuperuser  

**2. admin에 Model 신규 추가**
  - admin.py 파일 열기
  - 모델 등록 : admin.site.register(Menu)