# 	django서버 heroku에 배포하기

1. Heroku 설치 & 계정생성

2. Heroku App 만들기
   먼저 헤로쿠에 로그인을 하고

   ```shell
   Heroku login
   ```

   앱을 만들어준다.

   ```
   heroku create 
   ```

   이 때, app 이름은 랜덤으로 결정되는데 create 뒤에 app이름을 써주면 원하는 이름의 app을 만들 수도 있다.
   app이 만들어 졌다면

   ```shell
   git remote -v 
   ```

   명령어를 통해 heroku 주소가 연동이 잘 되었는지 확인해보자.
   

   **만약**

   remote주소를 바꾸고 싶다면 

   ```
   heroku git:remote -a herokuapp이름
   ```

   명령어를 통해 바꾸자.
   
3. django_heroku 모듈 설치

   ```
   pip install django_heroku
   ```

   를 설치하고 settings.py 맨 아래에 아래의 코드를 추가한다.

   ```
   import django_heroku
   
   django_heroku.settings(locals())
   ```

   

4. .git ignore 에 

   ```
   .vscode
   venv
   *.sqlite3
   .env
   *.bak
   ```

   을 추가해서 이상한게 올라가지 않도록 해주자

   

5. requirements.txt 파일 생성해줘야댐, 이 파일은 헤로쿠가 만드는 리눅스 서버에 어떤 파이썬 모듈을 설치해야하는지 알려주기 위함임. 
   requirements.txt를 만들기 위한 명령어는

   ```shell
   pip freeze > requirements.txt
   ```

   pip freeze는 가상환경에 설치된 파이썬 라이브러리 목록을 출력해주는 명령어임. > 명령어는 실행결과를 파일에 담아주는 역할을 함.

6. Procfile 만들기. 앱의 루트 디렉토리에 Procfile 이라는 이름의 파일을 생성하고 아래의 내용을 복사붙여넣기 한다.

   ```
   web: gunicorn 프로젝트이름.wsgi --log-file -
   ```

   gunicorn은 runserver 명령어임.

4. runtime.txt 만들기. 헤로쿠 서버에 우리가 올리는 파일이 어떤 버전의 파이썬을 사용하고 있는지 알려줘야한다. 루트 디렉토리에 runtime.txt 파일을 만들고

   ```
   python-3.7.4
   ```

   와 같이 적어준다. 이때 띄어쓰기 ㄴㄴ 대문자 ㄴㄴ

5. settings.py에 static root를 지정해주어야 한다. static root를 지정해 주는 것은 프로그램의 모든 스태틱 파일들을 한 디렉토리 아래에 넣고 관리하려고 하는 것이다. 이렇게 하는 이유는 페이지가 로드 될 때 스태틱 파일의 검색시간을 줄여주기 위함이다. 이러한 과정을 Pipelining이라고 한다.
   settings.py에 

   ```python
   STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
   ```

   위의 코드를 적어주고

   ```shell
   python manage.py collectstatic
   ```

   명령어를 실행하면 루트/staticfiles 에 스태틱 파일들이 모아진다.

6. SECRET_KEY와 DEBUG 환경변수로 돌리기 decouple을 이용해 settings.py의 SECRET_KEY와 DEBUG의 값을 숨겨주고 헤로쿠 홈페이지에 앱 페이지에 setting에 들어가 config vars를 추가해준다. DEBUG를 설정변수로 두는것은 True False를 쉽게 변경하기 위함이다.

7. 앱을 서버에 올리기전에 마지막으로 settings.py에 

   ```
   ALLOWED_HOSTS = []
   ```

   에 

   ```
   ALLOWED_HOSTS = [
   	'app이름.herokuapp.com',
   ]
   ```

   을 추가해주고

   ```shell
   python manage.py makemigrations
   ```

   을 통해 데이터베이스 구조를 만들어준다.

   장고는 기본적으로 sqlite3를 사용하지만 헤로쿠는 PostgreSQL을 사용한다. 하지만 걱정할필요 없다. heroku가 알아서 다 설정해주기 때문에 더 설정해줘야 될 것은 없다. + migrate는 할 필요없다 어차피 db파일은 서버에 안올릴 것이기 때문에 서버에 올린후 migrate 해주면 된다.
   
8. 헤로쿠는 git remote repo를 이용해 프로그램을 서버에 올려준다. 그러므로 헤로쿠에 장고앱을 올릴 땐  원격저장소에 push하는 것과 마찬가지로 git add > commit > push를 통해 올리게 된다. 그러므로

   ```shell
   git push heroku master
   ```

   와 같이 heorku라는 이름으로 등록된 remote url에 master 브랜치를 올려줘. 라는 명령어를 통해 장고앱을 배포할 수 있다.

9. 배포 후엔 heorku 홈페이지에 console로 가서

   ```
   python manage.py migrate
   python manage.py createsuperuser
   ```

    를 해주거나, heroku login이 되어있다면 로컬 bash창에서

   ```
   heroku run bash
   ```

   명령어를 통해 heroku 서버에 접속하여 cli를 작동시켜 볼 수 있다. 
   다만 heroku run 명령어는 방화벽에 의해 차단될 수 있다.



