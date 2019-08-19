# Django

- MVC() : 이게 주로쓰는 기본 패턴 

- MTV(Model Template View) : 그런데 장고에서는 이걸씀
  - Model : 데이터를 관리 models.py
  - Template : 사용자가 보는 화면 
  - View : 중간관리자, 제일중요함 views.py
- 

- django-admin startproject 이름 . 
  - 장고가 알아서 startproject들을 세팅해줌
- 장고의 관례
  - 대문자로만든 폴더명 아래에 같은이름의 소문자 폴더로 관리함



python manage.py runserver : 서버를 돌림

python manage.py startapp [앱이름] : 앱을만듬

settings.py 장고의 설정이 다들어가있음

urls.py : 페이지 경로가 여기에 들어감 여기서 머할지는 views.py에서 정의함 urls 가 문지기임.

manage.py 스크립트 돌릴때만쓰는애 직접 건드릴일 거의 없음



장고는 전체 크기구조는 project라는 이름으로 불리게됨  프로젝트안에 세부적인 app들이 들어감. 로직별로 앱을 구분해서 씀 (ex. 게시판앱, 회원관리앱, 영화평점 앱 등등)

python manage.py 



view에서 html 문서를 전달하는 것이 아니라 httpresponse라는 객체를 전달함 

플라스크는 진자를쓰고 

장고는 장고템플릿랭귀지를 씀 같아보이지만 다름

장고 DTL

model fat <- MTV MVC의 대원칙, model을 fat하게 만들고 template은 가볍게!

csrf cross site refference



### Template inheritance

1. 공통적으로 쓸 템플릿(code)을 뽑아낸다.
   - 
2. 해당 파일을 따로 만들고,
3. 활용할 다른 템플릿 파일에서 불러와 쓴다.

{% block 이름%} {% endblock %}

부분을 구성하는 template 이름은 언더바(_)를 붙여준다 ex. _nav.html

partilal rendering은 {% include '파일명.html' %} 을 사용



1. 사용자의 입력을 받아

   /artii/

2. artii api를 통해 ascii art를 보여주는 앱.

   /artii/result





LINTER, LINTING 문법 강제로 지키게 오류처럼 띄워주는 것.

