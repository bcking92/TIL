// python
// name = 'kim'
// print(name)

// js의 주석은 '//' 이다.
let x = 1
x = 2

if (x == 2){
    let x = 3
    let y = 4

    console.log(x)
}

console.log(x)
// console.log(y)

const MY_FAV = 3

console.log('내가 좋아하는 숫자는 ' + MY_FAV)
console.log(`내가 좋아하는 숫자는 ${MY_FAV}`)

MY_FAV = 20

// var 를 이용해 변수를 설정할 수도있는데 쓰지않는다. 
// 이유는 hoisting 때문임. var로 선언하면 코드가 실행되기전에 
// var로 선언한 변수가 문두로 올라가는 효과를 가짐.

// 저장은 (무엇을, 어디에, 어떻게(=)) 저장하는지!
//  - typeof 키워드를 이용해 알아보자
//  - 원시자료형, 기본자료형(primitive types, 그냥 언어자체에서 가지고 있는 자료형): 
//  - 숫자(아무숫자, (-)Infinity, NaN))) / 글자('', "", ``) / 불리언(false, true) / Empty Value: undefined(언어가 자동으로 생성하는 친구), null

//  1. 무엇을(자료형, datatype) 언어마다 약간씩 다름
//  2. 어디에(identifier 변수명, container type 자료 저장소의 종류)
//  - 이름을 정하는 JS의 관례
//  - 상수명 : ALLCAP
//  - 변수명, 함수명 : camelCase
//  - 클래스 : PascalCase
//    