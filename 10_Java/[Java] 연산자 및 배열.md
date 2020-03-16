# [Java] 연산자 및 배열

### 산술 연산자

- 정수형, 실수형에 사용

- `+`, `-`, `*`,`/`,`%`,`++`,`--`

  ```java
  int count = 1;
  int total = ++count; // count 1이 2로 증가된 후 할당
  int total = conut++; // count 값이 2에서 할당 되고 증가
  ```

<br>

### 비교연산자

- 대소 비교, 객체의 타입 비교등에 사용
-  `>`, `>=`, `<`, `<=`, `==`, `!=`, `instanceof`
- 연산결과는 boolean

<br>

### 논리연산자

- 논리형(boolean) 데이터 타입에 적용된다.
- 연산결과로 boolean을 가진다.
- `&`, `&&`, `|`, `||`, `!`

### 비트연산자

- 값을 비트(bit)로 연산하는 연산자

- `&`, `|`, `^`, `~`, `>>`, `>>>`, `<<`

### 기타연산자

- 대입 연산자
  - `=`, `+=`, `-=`, `*=`, `/=`, `%=`, `|=`, `^=`, `<<=`, `<<<=`, `>>=`
- 조건 삼항 연산자
  - `조건 ? 값 : 값`

### 배열

- 같은 타입의 데이터를 저장

- 객체로 취급한다.

- 생성

  ```java
  int scoreList[];
  scoreList = new int[100];
  // 또는
  int[] scoreList;
  scoreList = new int[100];
  // 또는
  int scoreList[] = new int[100];
  // 또는
  int[] scoreList = new int[100];
  // 또는
  int[] scoreList = { 45, 80, 100, 12, 33 };
  // 또는
  scoreList = new int[] { 45, 80, 100, 12, 33 };
  ```

- `length`, `index` 사용가능

  ```java
  scoreList.length
  scoreList[1]
  ```

- 다차원 배열 선언

  - `[][][]` 같이 만들어낸다.

    ```
    scoreList = new int[3][4];
    // 또는
    String[][] scoreList = new String[3][4];
    // 또는
    int[][] scoreList = new int[3][];
    scoreList[0] = new int[2];
    scoreList[1] = new int[2];
    scoreList[2] = new int[2];
    ```

##### 명령행 매개변수

```java
public class hello {
    public static void main(String args[]) {
        // 실행코드
    }
}
```

- 문자열의 배열을 매개변수로 받아서 프로그램 실행 시 필요한 정보를 프로그램에 전달하는 변수

- 공백(Space)를 구분자로 하여 여러개의 값을 전달한다.

  `apple grape pineapple`

- 명령행 매개변수 넣고 실행하기
  - Run -> Run Configurations

