# 00_variable

- JavaScript에서 변수 할당은

  - let
  - var
  - const

  등등의 키워드에 의해서 이루어 진다.

```javascript
let x = 1
```

먼저 let 키워드를 이용해 이렇게 변수를 선언하고 값은 할당해 놓으면

```javascript
x = 2
```

위와 같은 코드를 통해 변수의 할당 값을 변경할 수 있다.

하지만 이 코드 밑에 아래와 같이 다시한번 let 키워드로 같은 이름의 변수를 선언하는 것은 불가능하다.

```javascript
let x = 2
```

이 코드를 실행하게 된다면 already declared 라는 오류를 내게 된다.



const 키워드를 사용해서 변수 선언, 할당을 해보자.

```javascript
const x = 1
x = 2
```

위의 코드는 let 키워드로 선언한 변수와 다르게 오류가 난다. const 키워

