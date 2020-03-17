# [Java] 클래스(Class)의 구조

### 클래스의 멤버 구성

클래스(Class)는 선언부와 몸체로 나뉘고 몸체에는 클래스의 멤버가 선언된다. 멤버에는

- 객체의 초기화를 담당하는 생성자(Constructor), 파이썬으로 치면 `__init__()`
- 클래스가 가지는 속성을 정의하는 멤버 변수(Variable)
- 클래스가 가지는 데이터를 조작하고 변환하는 메서드(Method)

```java
public class Employee { //클래스 선언부
    // 멤버 변수
    private String name;
    private int number;
    private String dept;
    
    // 생성자
    public Employee(String name, int number, String dept) {
        this.name = name;
        this.number = number;
        this.dept = dept;
    }
    
    //메서드
    public String getName() {
        return name;
    }
    public void setName(String name) {
        this.name = name;
    }
    public String getnumber() {
        return number;
    }
    public void setNumber(int number) {
        this.number = number;
    }
    public String getDept() {
        return dept;
    }
    public void setDept(String dept) {
        this.dept = dept;
    }
}
```

<br>

### Modifier

- 접근 권한, 활용방법을 제어할 때 사용하는 예약어

- Modifier는 `class`, `variable`, `method`  등에 지정된다.

- 종류

  - 접근 권한 관련

    - `public`
      - [**Class, Variable, Method**] 모든 클래스에서 접근이 가능한 **클래스, 변수, 메서드**임을 의미한다.
    - `protected`
      - [**Class, Method**] 동일 패키지에 속하는 클래스와 하위 클래스 관계의 클래스에 의해 접근이 가능함을 의미한다.
    - `private`
      - [**Variable, Method**] **변수, 메서드**가 선언된 클래스 내에서만 접근이 가능하다는 것을 의미한다.

  - 활용 방법 관련

    - `final`

      - [**Class**] 자식 클래스를 가질 수 없는 **클래스**임을 의미한다. 상속 금지.
      - [**Varible**] **변수**를 **상수**로 이용하는 경우 사용한다. 단 한번 초기화 할 수 있으며 그 이후 초기화 불가능하다.  `final` + `static` 같이 사용.
      - [**Method**] Overriding이 불가능한 **메서드**를 정의할 때 사용한다.

    - `abstract`

      - [**Class**] 객체 생성이 불가능한 추상클래스를 의미한다. `interface` 와 비슷하다. 

        - 추상 메서드를 포함하는 클래스는 추상 클래스로 정의되어야 한다. 그 반대는 아님.

      - [**Method**] 추상 메서드를 의미한다. 추상 메서드는 하위 클래스에 의해 구현된다.

        - 추상 메서드는 메서드의 시그니처(리턴 타입, 메서드명, 매개변수)만 정의되고 구체적인 행위(블록 부분)은 정의되지 않은 메서드를 말한다.

          ```java
          abstract int sum(int num1, int num2);
          // {} 부분은 작성하지 않는다.
          ```

    - `static`

      - [**Variable, Method**] 클래스에 소속된 **클래스 변수, 클래스 매서드**를 의미한다.
      - `static`이 붙지 않으면 생성된 인스턴스마다 해당 변수, 메서드가 포함된다.
      - `static`이 붙으면 생성된 인스턴스에 포함되지 않고 많은 인스턴스를 생성하더라도 메모리에 하나의 변수, 메서드만 존재한다. 클래스 변수와, 클래스 메서드는 객체를 생성하지 않고도 접근할 수 있다.
      - 클래스 메서드는 인스턴스 변수를 참조할 수 없다.
      - 클래스 변수는 python에서 클래스 변수를 정의하는 것과 동일한 개념이다.

    - `synchronized`

      - [**Method**] Thread의 동기화를 위한 메서드이다.

##### 멤버 변수 접근 권한

| 종류        | 클래스 | 하위 클래스 | 동일 패키지 | 모든 클래스 |
| ----------- | ------ | ----------- | ----------- | ----------- |
| `private`   | O      | X           | X           | X           |
| `(default)` | O      | X           | O           | X           |
| `protected` | O      | O           | O           | X           |
| `public`    | O      | O           | O           | O           |

- modifier를 통해 **정보 은닉**을 구현한다.

<br>

### 객체 생성

```java
// 참조 변수 선언
// 클래스이름 변수이름;
Car mycar;

// 클래스로 부터 객체 생성
mycar = new Car();
```

<br>

### Getter와 Setter

- 멤버 변수들은 대부분의 경우 `private`로 선언해서 외부에서는 숨겨진 형태로 만든다.
- public으로 지정한 메서드를 통해 멤버 변수에 접근하는 것이 **정보은닉의 기본**이다.
  - `getXXX()`, `setXXX()`, Getter, Setter라고 한다.

### 생성자(Constructor)

- 생성자는 클래스로부터 객체를 생성할 때 호출되며, 객체의 멤버 변수를 초기화 하는데 사용되는 메서드이다.

  ```java
  public class practice {
  	public static void main(String args[]) {
  		person babo;
  		babo = new person("짱구", 23);
  		System.out.println(babo.getName());
  		System.out.println(person.company);
  		System.out.println(babo.getTitle());
  		System.out.println(babo.getAge());
  	}
  	
  	public static class person {
  		private String name;
  		private int age;
  		private String title;
  		private static String company = "S전자";
  		
  		public person(String name, int age) {
  			this.name = name;
  			this.age = age;
  			this.title = "사원";
  		};
  		public String getName() {
  			return name;
  		}
  		public void setName(String name) {
  			this.name = name;
  		}
  		public int getAge() {
  			return age;
  		}
  		public void setAge(int age) {
  			this.age = age;
  		}
  		public String getTitle() {
  			return title;
  		}
  		public void setTitle(String title) {
  			this.title = title;
  		}
  		public static String getCompany() {
  			return company;
  		}
  		public static void setCompany(String company) {
  			person.company = company;
  		}
  
  	};
  ```

  - 생성자는 클래스와 같은 이름을 가진다.
  - 생성자는 반환형(Return Type)이 없다. (void도 안됨)
  - 생성자는 여러개를 Overloading 할 수 있다.
  - 생성자는 키워드 `new`와 항상 같이 사용된다.
  - 작성하지 않을 경우 기본 생성자가 제공된다.

- **생성자와 Modifier**
  - `public`
    - 모든 클래스에서 접근 가능하다.
  - `protected`
    - 동일 패키지에 속하는 클래스와 하위 클래스 관계의 클래스에 의해 접근이 가능하다.
  - `private`
    - 클래스 내에서만 접근이 가능하다. 
- **기본 생성자(Default Construtor)**
  - 클래스에 생성자가 없을 경우 컴파일러에 의해 자동으로 생성되는 생성자