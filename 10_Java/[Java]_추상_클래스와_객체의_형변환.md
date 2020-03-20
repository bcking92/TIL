# [Java] 추상 클래스와 객체의 형변환

### 추상 메서드

- 메서드의 시그니쳐(리턴타입, 메서드명, 매개변수)만 정의한 메서드.

- `abstract` 예약어를 통해 생성 가능

  ```java
  abstract returnType name([argType argName, ...]);
  ```

### 추상 클래스

- 일반적으로 하나 이상의 추상 메서드를 포함한다. (없어도 상관은 없음)
- 추상 메서드를 하나 이상 가지고 있다면 추상 클래스로 선언해야 한다.(강제)
- 추생 클래스는 객체를 생성할 수 없다.

##### 추상 클래스와 추상 메서드는 왜 필요할까?

- 메서드의 오버라이딩을 강제할 수 있다. == 자식 클래스들의 메서드를 통일할 수 있다. -> 최소한의 수정으로 원하는 객체를 사용할 수 있다. -> 유지보수가 쉬워진다.

### 내부 클래스

- 클래스가 다른 클래스를 포함하는 경우 내부에 포함된 클래스를 내부 클래스라고 한다.
- 내부 클래스는 파일 크기의 최소화, 보안, 성능 향상, 이벤트 처리 등을 쉽게 하기 위하여 사용된다.
- 정의되는 위치에 따라서 멤버 클래스와 지역 클래스로 나뉜다.

##### 멤버 클래스

- instace 멤버 내부 클래스
  - 클래스의 멤버와 동일한 위치에서 선언되는 내부 클래스
  - 다른 외부 클래스에서도 사용 가능하다.
- static 멤버 내부 클래스
  - 외부 클래스의 객체를 생성하지 않고 내부 클래스 객체를 생성할 수 있다.

###### 지역 클래스

- 이름이 있는 지역 내부 클래스
  - 메서드 내부에서 정의된 클래스로서 지역 변수와 동일한 범위를 가진다.
  - 클래스 이름이 명시된다.
  
- 이름이 없는 지역 내부 클래스

  - 이름을 갖지 않는 내부 클래스
  - `new` 예약어 뒤에 명시된 클래스가 기존의 클래스인 경우 자동적으로 이 클래스의 자식 클래스가 된다.
  - 추상 클래스의 객체를 내부 클래스 형태로 생성할 때 자주 사용된다.
  - 이름이 없는 지역 내부 클래스를 이름이 있는 클래스로 구현하면 복잡해지는 소스 코드를 명확하게 할 수 있고 재사용성을 높일 수 있다.

  ```java
  new Class() {
      // overriding
  } // 형식으로 작성
  ```

<br>

### 형변환

- 묵시적 형변환(Promotion)
  - 형변환 연산자를 사용하지 않아도 자동으로 이루어지는 경우(자동 형변환)
  - 작은 값 -> 큰 값
- 명시적 형변환(Demotion)
  - 더 작은 범위를 나타내는 데이터 타입으로 변환되는 경우(축소 형변환)
  - 큰 값 -> 작은 값
  - 정보를 잃을 수 있기 때문에 명시적으로 해줘야한다.

### 객체의 형변환

객체 참조변수의 경우에도 형변환(casting)이 이루어진다.

##### 조건

- 객체의 유형이 서로 상속 관계에 있는 경우

##### 묵시적 형변환

- 왼쪽 객체가 오른쪽 객체의 상위 클래스인 경우에만 묵시적 형변환이 일어난다.

  ```java
  Car car = sedan
  ```

##### 명시적 형변환

- 할당되는 인스턴스 유형에 따라서 실행 오류가 발생할 수 있으므로 주의해야 한다.
- `instanceof` 연산자를 이용해 판단한다.

- `instanceof`

  - 생성된 객체가 class와 관계있는 형(type)으로 만들어졌는지 확인한다.

  - `true` 또는 `false`를 반환한다.

    ```java
    class Employee {
    }
    class Manager extends Employee {    
    }
    
    public class InstanceOfTest{
        public static void main(String args[]) {
            Manager m = new Manager();
            Emploee e = new Employee();
            System.out.println(m instanceof Manager); // m이 Manager 형이므로 true
            System.out.println(m instanceof Employee); // m이 Employee 형이므로 true
            System.out.println(e instanceof Manager); // e가 Manager 형이 아니므로 false
        }
    }
    
    ```

### 형변환과 멤버 변수

형변환에 참여한 서로 상속 관계에 있는 두 클래스 간에는 동일한 이름의 변수가 존재하거나 메서드가 Overriding 되어 있을 수 있다. **그러므로 생성된 객체 변수를 통해 멤버에 접근할 때 주의해야 한다.**

```java
class Parent {
    int num = 10;
    
    void printNum() {
        System.out.println(num);
    }
}
class Child extends Parent {
    int num = 20;
    
    void printNum() {
        System.out.println(num);
    }
}

public class ObjectCastTest {
    public static void main(String args[]) {
        Parent p = new Child();
        p.printNum();
        System.out.println(p.num);
    }
}
// 실행 결과
// 20
// 10
// 첫번째 printNum() 에서는 Child 객체에 Overriding 된 printNum() 메서드를 호출한다.
// 두번째 println(p.num) 에서는 Parent 객체의 num 값을 출력한다.
```

- 위와같은 결과가 나오는 이유
  - 변수에 대한 접근은 객체의 유형에 따라 결정된다.
  - 메서드 호출은 할당되는 인스턴스에 따라 결정된다.
  - 이것은 객체 참조 변수가 **변수**나 **메서드**를 참조하는 경우, **참조 관계를 결정하는 시간**이 **다르기** 때문에 나타는 차이이다.



