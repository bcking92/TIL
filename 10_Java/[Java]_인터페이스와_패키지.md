# [Java] 인터페이스와 패키지

### 인터페이스와 다형성

#### 인터페이스(interface)

- 추상 클래스보다 추상성이 더욱 심화된 개념이다.
- 멤버 변수는 모두 상수형으로 선언되어야한다.
- 메서드는 모두 추상 메서드로 선언되어야 한다.

##### 인터페이스를 사용하는 이유?

- 논리적으로 'is a ~' 관계가 성립하지 않는 경우
- 다중상속을 받고 싶은 경우

위와 같은 상황에서 인터페이스를 사용하여 문제를 해결할 수 있다.

##### 인터페이스의 정의

```java
public interface 인터페이스명 [extends 부모인터페이스, ...] {
    // 멤버 변수를 상수로 정의
    // 추상메서드
}
```

```java
public interface Drawble {
	public static final int PALIN_PEN = 1;
    public static final int BOLD_PEN = 2;
    public static final int ITALIC_PEN = 3;
    public abstract void draw();
    public abstract void move(int x, int y);
}
// 인터페이스의 변수 선언에 사용된 static final이나 메서드 선언에 사용된 abstract는 생략할 수 있다.
```



#### 인터페이스의 활용

- 인터페이스를 상속 할 땐 `implement` 예약어를 사용한다.

  ```java
  [modifier] class [클래스이름] [extends 부모 클래스] [implements 인터페이스1, 인터페이스 2, ...] {
      
  }
  ```

- 인터페이스를 상속하는 클래스는 인터페이스에 정의된 추상 메서드들을 반드시 Overriding 해야한다.

  - 메서드를 하나라도 Overriding 하지 않을 경우 해당 클래스는 추상 클래스로 선언해야 한다.

### 객체지향 언어의 주요 개념

#### 패키지의 개요