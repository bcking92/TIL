# JavaScript 기초

OOP

Object는 두가지만 있으면 된다.

1. property : 자기의 고유의 값, 특성을 가지고 있다.
2. method : object를 조작하는 method를 가지고 있다.



Javascript를 브라우저에서 분리하여 사용하게 해주는 것 => node.js 

js는 브라우저만 조작하는 언어였지만 c, java, python 과같이 일반적인 프로그래밍언어로 쓰기 위해 만들어진 것이 node.js

let으로 두번 선언할 수는 없다.

let 키워드는 이미 같은이름의 변수가 있는 공간에는 중복선언을 할 수 없다.

재할당을 하려면 변수이름 = 값 의 형태만 적어주면 된다.

let 을 붙이지 않고 변수를 할당할 수도 있지만 그렇게 되면 전역변수로 설정된다. 되도록이면 안쓰는 것이 좋다.

let 은 블록스코프(block scope)라는 것을 해주는 것이다. 중괄호안에 있는 부분이 블록스코프임

```js
let x = 1

if (x == 1){
    let x = 3
    
    console.log(x)
}

console.log(x)
```

let 은 변수를 만들어줬다면

const는 상수를 만들어준다. <- 변하지 않는다. = 변경할 수 없다. 상수명은 모두 대문자로 적어주는 것이 컨벤션

이게 무슨말이냐 Assign과 Declare는 다른 것이다. 

Assign은 변수, 상수에 값을 할당하는 것이고 Declare는 변수, 상수가 있다고 선언하는 것이다.

그런데 const는 re assign과 de declare 둘다 불가능하고 let은 re assign은 되지만 re declare는 불가능하다. 이말이다.





# 새로운 프로그래밍 언어를 맞이 했을 때 배우는 꿀팁

- 먼저! 저장, 계산, 조작을 배워보자
  - 내가 알고있는 언어와 문법적인 차이를 본다.
  - 그 언어의 관례를 본다.
  - 함수까지는 본다.
  - class까지는 봐도 되고 안봐도 되고 그렇다.





- 위의 정도와 한다음에 구현을 해본다. 실제 피쳐를 만드는 것이다.
  - 예를 들면 내가 원래 언어로 할 수 있었던 것을 새로운 언어로 구현해보는 것이다.
- 책 목차대로 해보는 것은 비효율적이다.



non-blocking

(asynchronous)



JavaScript 에서는 함수의 정의 위치가 아래에 있어도 위에서 사용할 수 있다.(asynchronous)

JavaScript 는 기본적으로 synchronous하지만 asynchronous하게 구현된 함수들이 많다.

MTTM 

데이터는 기본적으로 010101로 들어가기 때문에 한번에 전송할 수 없다. TCPIP는 데이터들을 쪼개서 보낸다다. 데이터의 가장 작은 단위는 패킷

엔드포인트가 가지고있는 인증서 2개랑 비교함 HTTPS





tracert = trace router 

router 스위치는 주소암호를 판단

coursera bit & bite of Computer networking