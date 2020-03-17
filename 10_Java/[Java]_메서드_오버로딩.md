# [Java] 메서드 Overloading과 매개변수

### 메서드 오버로딩(Overloading)

- 데이터 타입이 달라도 변수의 중복선언은 허용되지 않지만 Java에서 메서드는 오버로딩(중복정의)이 가능하다.
- 동일한 이름의 메서드라도 매개변수의 개수와 타입만 다르면 다른 메서드로 인식한다.

### 오버로딩이 필요한 이유

```java
public void printInt(int data) {
}
public void printDouble(double data) {
}
public void printChar(char data) {
}
public void printString(String data) {
}
```

- 위와 같이 너무 많은 다른 메서드가 필요하고, 코드 재사용이 어렵게 된다.
- 메서드를 호출하는 코드에서 문제가 발생한다.

### 메서드 오버로딩 유형

- 매개변수의 개수와 타입이 모두 다른 경우
- 매개변수의 개수와 타입이 같지만 순서가 다른 경우
- 매개변수가 형변환된 다른 타입인 경우
  - 매개변수의 묵시적 형변환이 일어나면 오버로딩 가능하다.

### 주소복사

```java
int[] list = {100, 85, 99};
int[] copyList = list;
```

- shallow copy가 일어난다. 

### 매개변수 전달 방식

##### 기본형 매개변수

- `int`, `char`

##### 참조형 매개변수

- `int[]`, `String[]`

##### 매개변수로 객체 넘기기

- `Car`

##### 가변적 매개변수

```java
public int sum (int... num) {
    
    // ...
}
```

- 가변적 매개변수는 매개변수 리스트의 마지막 위치에서만 사용 가능하다.