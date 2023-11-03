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


