## 배포
  **1. 디버그 모드 false 설정** : `DEBUG = False`

  **2. ALLOWED_HOSTS 설정**  
    - `ALLOWED_HOSTS = ['.pythonanywhere.com']` >> 점 꼭 찍어줘야함!!!!

  **3. 정적 파일 수집**  
    - `STATIC_ROOT = os.path.joion(BASE_DIR, 'static')` 👉🏻statc 디렉토리를 STATIC_ROOT로 설정  
    - python mange.py collectstatic
  
  **4. 프로젝트 디렉토리 압축**

  **5. pythonanywhere 접속, 압축 파일 업로드**

  **6. unzip [파일명]**

  **7. python 가상환경 세팅 및 실행**  
    - `virtualenv --python=python3.7 [가상환경 이름]`  
    - 가상환경 디렉토리 이동, `source bin/activate`  
    - `pip install django==[버전]`  
    - 우측 상단 >> Web 이동  
    - Add a new web app, Manual configuration, Python버전  
    - **생성 후 하단의 Code 수정**  
      * Source Code : `/home/{id}/{프로젝트명}`
      * Working directory : `/home/{id}/`
      * WSGI(wsgi.py) 파일 수정

  - **wsgi.py 수정 내용**
    * ✏️주석✏️ 19:47  `HELLO WORLD ~ yiend content.encode('utf8)`
    * ✏️주석 해제✏️ 75:89(DJANGO 부분)
    * ✏️path 수정✏️  `path = '/home/kimdaewhi/[django 프로젝트명]'`  
    * ✏️settings.py 경로 수정✏️ `os.environ['DJANGO_SETTINGS_MODULE'] = 'costaurant.settings'`  

  **8. 저장 및 Virtialenv 설정**  
    - 가상환경 경로 설정 `/home/{ID}/{가상환경 명}`

  **9. 정적파일 경로 세팅**  
    - ✏️URL >> `/static/`
    - ✏️Directory >> `/home{id}/{프로젝트명}/{static directory 명}`