





data를 관리하는 방법은 django의 orm을 이용하는 방법이 있었음.

이때  ORM은 파이선의 객체를 건드려서 sql query(sqllite) 를 작성해 데이터를 컨트롤 하는 것임.

하지만 RDMBS은 sqllite말고 다른 sw들도 많음



# 데이터베이스(DB)

데이터베이스는 체계화된 데이터의 모임임

여러사람이 공유하고 사용할 목적으로 통합 관리되는 정보의 집합이다.

논리적으로 연관된 하나 이상의 자료의 모음으로 그 내용을 고도로 구조화함으로써 검색과 갱신의 효율화를 꾀한 것



# SQLlite 설치하기 & 사용하기

SQLlite DLL 과 SQLlite tools를 다운로드 받는다.

1. 원하는 폴더에 저장하기
   - home 으로 와서(cd ~) sqlite폴더 만들기(mkdir sqllite)
   
     ```shell
     cd ~
     mkdir sqllite
     ```
   
     
   
   - 받은 파일을 다 여기로 옮김( 폴더 빼고 파일만)
   
     ```shell
     mv ~/sqllite/sqldiff.exe .
     mv ~/sqllite/sqlite3.def .
     mv ~/sqllite/sqlite3.dll .
     mv ~/sqllite/sqlite3.exe .
     mv ~/sqllite/sqlite3_analyzer.exe .
     ```
2. 경로 설정
   
   - 환경변수에 sqllite3의 path를 저장해 준다.
   
     



사용할 때는 interactive shell의 종류를 바꿔주어야 한다.

깃배쉬는 cygwin, winpty 등등을 쓰고있음. 그런데 sqlite는 winpty에서만 열림

그러므로 `winpty sqlite3`라고 해줘야 열수 있음.

열고 `winpty sqlite3`를 bashrc alias를 이용해 'sqlite3'라고 줄여서 사용하자

sqlite3 --version <- version을 보자

sqlite3 db.sqlite3 처럼 뒤에 파일명을 이용해 sqlite3파일을 열 수 있음 파일이 없으면 파일을 만들어버림

실행후 .exit을 입력하면 나갈 수 있음



| 명령어                                                | 기능                                                         |
| ----------------------------------------------------- | ------------------------------------------------------------ |
| `.databases 데이터이름`                               | 데이터의 저장 위치를 보여줌,                                 |
| `.table`                                              | 테이블을 다 보여줌                                           |
| `.exit`                                               | sqlite3 종료                                                 |
| `SELECT * FROM posts_post;`                           |                                                              |
| `SELECT`                                              | 가져올 열의 이름을 입력함, 모두 가져오려면 *을 이용          |
| `FROM`                                                | 어느 테이블에서 가져올지 선택함, * 사용 불가                 |
| `.headers on`                                         | 데이터를 볼 때 header를 달아줌                               |
| `.mode column`                                        | 데이터를 볼 때 칸나눠서 보여줌                               |
| `CERATE TABLE 테이블이름(컬럼이름 타입 키여부, ...);` | 테이블을 만듬                                                |
| `.schema 테이블이름`                                  | 테이블의 schema를 확인함                                     |
| `DROP TABLE 테이블이름;`                              | 테이블 지우기                                                |
| `SELECT rowid`                                        | primary key를 정의 안했을 때 sqlite 가 자동으로 id를 부여해줌 |
| `NOT NULL`                                            | null을 허용하지 않는다. (null을 입력할 수 없음)              |
| `LIMIT number`                                        | 테이블에서 데이터를 숫자만큼  가져옴                         |
| `LIMIT number OFFSET number`                          | 앞의 offset 숫자 개수의 데이터를 제외하고 그 다음 limit 숫자 개의 데이터를 가져옴 |
| `WHERE column=value`                                  | column이 value값을 가지는 데이터 가져오기                    |
| `SELECT DISTINCT column`                              | 해당 컬럼의 데이터중복을 피해서 가져오기 (데이터의 범위보기) |
| `DELETE FROM table WHERE condition`                   | 해당 table에서 condition에 맞는 것을 찾아서 다 지움          |
| `AUTOINCREMENT`                                       | 데이터가 삭제되도 비어있는 primary key를 재사용하지 않고 숫자를 계속 증가시켜준다. |
| `UPDATE table SET changes WHERE condition`            | 테이블에서 컨디션에 맞는 모든 데이터에 changes를 적용함      |
| AVG()                                                 |                                                              |
| MAX()                                                 | <br />                                                       |
| MIN()                                                 |                                                              |
| LIKE(와일드카드)                                      |                                                              |
| ALTER TABLE existing table<br />RENAME TO new table   | 테이블 이름 변경                                             |

- **sqlite 데이터 타입**
  - INTEGER(정수형)
    - TINYINT(1byte), SMALLINT(2bytes), MEDIUMINT(3bytes), INT(4bytes), BIGINT(8bytes), NUSIGNED BIG INT, 
  - TEXT(텍스트)
    - CHARACTER(20), VARCHAR(255), TEXT, 텍스트
  - REAL(실수)
    - REAL, DOUBLE, FLOAT, 실수
  - NUMERIC(숫자형)
    - NUMERIC, DECIMAL, BOOLEAN, DATE, DATETIME, 숫자형
  - BLOB(불리언 or 바이너리)
    - binary, TRUE, FALSE



### SQLlite의 CRUD

| 명령어                                                       | 기능                                                         |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| `INSERT INTO 테이블이름 (컬럼이름, 컬럼이름, 컬럼이름) VALUES (넣을값, 넣을값, 넣을값), (다음넣을값, 다음,다음), (그다음데이터, 그다음, 그다음)` | 테이블에 데이터 삽입하기, 모든테이블에 다 넣을거면 생략해도 상관, 한번에 여러개 넣기도 가능 |



### CSV 파일을 DB로 만들기

```sqlite
.mode csv  # == csv들어간다 입벌려라~
.import csv파일명 테이블명    # csv파일을 테이블명의 테이블로 db에 저장함 테이블이 없다면 자동으로 생성해줌
```

csv를 바로 db로만들면 schema가 이상하니까 먼저 table을 정의하고 csv를 불러오자

header exclusion 항상해주자!!



구멍이 송송난 DB를 만들고 싶지 않다면 shema를 tight하게 짜주는것 이 중요함.



#### SQLlite는 특별한 요구사항이 없으면 AUTOINCREMENT을 쓰지 않는 것이 관례임.( sqlite는 메모리가 부족한 기기에서 주로 쓰이기 때문에 메모리 관리를 위해서 그렇다고 함)  