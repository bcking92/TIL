function add(x, y) {
    return x + y
}

// function expression 함수표현식, 주로사용
const sub = function(x, y) {
    return x - y
}


// arrow function (ES6)
const mul = (x, y) => {
    return x * y
}

const ssafy = function(name) {
    return `안녕, ${name}`
}

const ssafy1 = name => {
    return `안녕, ${name}`
}

// 괄호를 없애는 조건은 인자가 1개만 있을때,
// 블락을 없애는 조건은 표현식이 하나만 있을 때, 
const ssafy2 = name => `안녕, ${name}`

// 이게 디폴트
const ssafy3 = () => {}
const ssafy4 = _ => {}

const square = function (num) {
    return num ** 2
}

const square2 = num => num ** 2

console.log(square2(3))

