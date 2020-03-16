# [Java] 제어문

### 조건 제어문

- `if`, `if-else`, `if-else if`, `switch`

#### `if`

```java
if(Expression) {
    Statement1;
}
```

#### `if-else`

```java
if (expression2) {
    Statement1
else {
    Statement2
}
```

#### `if-else if`

```java
if (expression2) {
    Statement1
} else if (expression2) {
    Statement2
} else {
    Statement3
}
```

#### `switch`

```java
switch (Expression) {
    case value1:
        Statement1;
        break;
    case value2:
        Statement2;
        break;
    case value3:
    case value4:
        Statement3;
        break;
    default;
        break;
}
```

<br>

### 반복 제어문

- `for`, `while`, `do-while`
- `do-while`은 무조건 한 번 이상 수행됨

#### `for`

```java
for (초기식; 조건식; 증감식) {
    Staement1;
}

for (int i = 0; i < 10; i++) {
    System.println.out(i);
}
System.println.out('끝');
```

- for 블록 내부에서 선언된 변수는 for 블록 내부에서만 사용 가능

#### `while`

```java
while (조건식) {
    Statement1;
}
```

- 애초에 조건식이 false이면 while로 안들어간다.

#### `do-while`

```java
do {
    Statement1;
} while (조건식);
```

- statement1을 한 번 실행하고 조건에 따라 또 실행할지 말지 결정한다.

#### `break`

- `for`나 `while` 블록 안에 break; 구문은 가장 가까운 반복 루프를 멈추게 한다.

  ```java
  while () {
      if() {
          break;
      }
  } 
  ```

  ```java
  for () {
      for () {
          break;
      }
  }
  ```

#### `continue`

- `for`나 `while` 블록 안에 continue; 구문은 아래 명령을 실행하지 않고 바로 반복문의 조건부로 실행위치를 옮긴다.

  ```java
  for () {
      if () {
          statement1;
          continue;
      } else {
      	statement2;
      }
  }
  ```

#### `label`

- `label`을 통해 `break`나 `continue`의 실행영역을 정해줄 수 있다.

  ```java
  outer: for () {
      for () {
          if () {
              break outer;
          }
      }
  }
  // 위의 코드는 break가 맨 위의 for문 까지 break 시킨다.
  ```

  ```java
  outer: for () {
      for () {
          if () {
              continue outer;
          } 
      }
  }
  // 위의 코드는 continue로 인해 실행위치가 outer for문의 조건부로 돌아가게 만든다.
  ```

#### `return`

- 함수 내에서 `return` 구문을 만나면 해당 값을 return하고 함수를 빠져나온다.