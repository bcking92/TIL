# 데이터베이스 기초(Dabta Base)

- 관계형 데이터베이스 :

  ​	관계 대수학을 기반으로 만들어짐

  ​	데이터의 구성이 x,y 로 펼쳐질수 있는 표를 통해서 나타나는 것.

- 데이터베이스의 구성요소

  	- 개체(entity)

  	- 속성(attribute)

   - 테이블(table) : 엑셀에서 sheet와 동일한 개념, table name이 있음. 행과 열로 이루어진 데이터의 묶음.
       - 열(Column), 컬럼, field
       - 행(Row, Tuple), 레코드
  - 키(Key)
    - PK(기본키, Primary Key) 
      -  각 행의 고유값으로 Primary Key라고 함. **반드시** 설정하여야 하며, 데이터베이스 관리 및 관계 설정시 주요하게 활용함. (ex, SKU, id)
    - 

  

  스키마(scheme) : 데이터가 어떤 특성인지 알려주는 데이터, 자료의 구조, 표현방법,관계등을 정의한 테이블 데이터베이스의 구조와 제약조건(자료의 구조, 표현 방법, 관계)에 관련한 전반적인 명세를 기술한 것.



- SQLite 
  - 장고의 기본 데이터베이스
  - 핸드폰의 자료저장도 이걸로 이루어짐 ( 가볍기때문에 )



데이터는 CRUD를 통해 제어됨.

C(reate)

R(ead)

U(pdate)

D(elete)



## ORM(Object-Relational Mapping)

개념 : 파이썬도 모든 것이 객체인데.. DB의 레코드(데이터),테이블 같은것도 객체로 바꿔서 이용해버리자!

Django ORM을 사용할 것임.

- models.py에 코딩한다
- python manage.py makemigrations = models.py에 있는 것을 토대로 장고가 데이터 설계도 만들어줌
- 이걸 실제로 적용하는 것을 migrate라고함.
- python manage.py migrate



python manage.py shell 장고앱이 돌아가는 모든 context가 있는 shell을 열어줌

from articles.models import Article

Article.objects.all() Article안에있는 오브젝트 다가지고와

Article.objects.first()

Article.objects.last() 등등 있음.



python manage.py createsuperuser admin 계정 만들기 python terminal에서 열기

## SQL(Structured Query Language)

- RDBMS(Related Data Base Managing System)의 데이터를 관리하기 위해 설계된 특수 목적의 프로그래밍 언어. RDBMS 자료의 검색과 관리 데이터베이스 스키마 생성과 수정, 데이터베이스 객체 접근 조정 관리를 위해 고안되었음.