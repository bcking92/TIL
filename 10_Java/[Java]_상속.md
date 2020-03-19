# [Java] 상속(Inheritance)

- 기본이 되는 클래스를 확장하여 새로운 클래스를 정의하는 것

- 부모의 모든 변수와 메서드를 자식이 물려받는다.

- extends 예약어를 통해 상속한다.

  ```java
  public class Comedian extends Person {
      
  }
  // person 클래스를 상속받아 comedian class를 만든다.
  ```

  - inheritance 대신 extends를 사용하는 이유는 상속에서는 추가적인 것들을 확장한다는 의미가 더 강하기 때문이다.

    상속 = 부모 기능 + **새로 추가되는 자식기능** 이기 때문이다.

- 상속을 하기 위해서는 부모 클래스와 자식 클래스의 관계가 일반화와 특별화의 관계에 있어야 한다.

  - 논리적으로 'is a~ 관계'에 있어야 한다. '{자식} is a {부모}'가 논리적으로 성립할 때 상속을 하는 것이 맞다.

### 단일 상속(Single inheritance)

- 자바에서 다중상속을 허용하지 않는 이유는 다중 상속과정에서 중복되는 변수와 메서드가 생기기 때문이다.

  - 다중 상속은 죽음의 다이아몬드(the Deadly Diamond of Death) 현상이 있다. 부모클래스가 2개이고 클래스에서 상속하는 변수나 메서드의 이름이 겹칠 경우 어떤 것을 선택해야 할지 결정하기 어렵다. 그렇다고 다중 상속을 염두해 두고 모든 변수나 메서드의 이름을 다르게 짓는 것은 불가능하기 때문에 자바에서는 애초에 단일 상속만을 허용하고 있다.

    ![dod](DiamondOfDeath.png)

### 생성자

- 상속된 클래스의 생성자가 호출 될 때 부모 클래스의 생성자가 같이 호출된다.
  - 이 때, 부모 클래스의 생성자가 먼저 초기화를 수행하고 -> 그 이후 자식 클래스의 초기화가 이루어진다.
  - 자식 클래스에 의해 호출되는 부모 클래스의 생성자는 별도로 지정하지 않는 경우 기본 생성자가 호출된다.
  - 부모 클래스의 기본 생성자가 없다면 에러가 발생한다.

##### this() 생성자, super() 생성자

- `this()`
  - 클래스 안에서 Overloading 된 또 다른 생성자를 호출하기 위해 사용한다.

- `super()`

  - 부모 클래스의 생성자를 명시적을 호출할 때 사용한다.

  - 부모 클래스의 생성자가 Overloading 되어 여러 개 존재하는 경우 특정 생성자를 호출하기 위해 사용한다.

```java
  class Shape {
      int x = 0;
      int y = 0;
      
      Shape() {
          this(0, 0);	// 클래스 내의 overloading된 Shape(int x, int y)를 명시적으로 호출한다.
      }
      Shape(int x, int y) {
          this.x = x;
          this.y = y;
      }
  }
  
  class Circle extends Shape {
      int radius;
      Circle(int x, int y, int radius) {
          super(x, y);	// 부모 클래스(Shape)의 Shape(int x, int y) 생성자를 명시적으로 호출한다.
          this.radius = radius;
      }
  }
```

  <br>

### 변수

- `Private` 변수는 상속에서 제외된다.
- 부모 클래스와 같은 이름의 변수를 자식 클래스에서 선언하면 부모 클래스의 변수가 상속에서 제외된다.
  - 클래스 변수, 인스턴스 변수 모두 적용된다.

##### this 예약어와 super 예약어

- `this`
  - 생성된 객체 자신에 대한 참조를 의미한다.
  - 멤버 변수와 메서드 매개변수의 이름이 같을 경우, 두 변수를 구분하기 위해 사용한다.
- `super`
  - 부모 객체에 접근할 수 있는 참조변수로 사용한다.

```java
class Employee {
    String name;
    int DeptNo;
    String grade;
}

class Manager extends Employee {
    String boss;
    char grade;
    
    void printGrade() {
        this.grade = 'A'; // 자기 자신의 grade를 의미한다.
        super.grade = "A등급"; // 부모 클래스의 grade를 의미한다.
    }
}
```

<br>

### 메서드

- 메서드 Overriding
  - 부모 클래스의 메서드를 재사용하지 않고 새롭게 정의하여 사용할 수 있다.
  - 메서드를 Overriding 할 때는 부모 클래스의 메서드 이름, 매개변수의 유형과 개수가 동일해야 한다.
    (그렇지 않으면 Overloading이 되어버린다)
  - 메서드를 Overriding 하면 부모가 가진 메서드가 상속되지 않는다. 

##### Overloading VS Overriding

- Overloading
  - 하나의 클래스에 동일한 이름의 메서드가 여러 개 중복 정의되어 있는 것.
  - 메서드 매개변수의 개수나 타입이 달라야 한다.
- Overriding
  - 상속 관계에 있는 두 개의 클래스에서 부모가 가진 메서드와 동일한 시그니처(리턴 타입, 메서드명, 매개변수)를 가진 메서드가 자식 클래스에 재정의되어 있는 것.

##### super 예약어

- 메서드를 Overriding 할 때 부모 메서드를 사용하고 싶다면 `super`를 통해 구현할 수 있다.

  ```java
  class Camera {
      String name;
      int sheets;
      
      public void takePicture() {
          System.out.println("Camera 찰칵");
      }
  }
  
  class PolaroidCamera extends Camera {
      int batteryGage;
      
      public void takePicture() {
          super.takePicture(); // 부모 클래스인 camera class의 함수를 호출한다.
          System.out.println("PolaroidCamera 현재 배터리: " + batteryGage);
      }
  }
  ```

##### final 예약어

- 메서드 Overriding을 금지한다. == 상속을 강제한다.

  