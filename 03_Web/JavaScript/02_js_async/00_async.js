const nothing = () => {
    console.log('3초 기다려')
}
console.log('start')

setTimeout(nothing, 3000)

console.log('end')

// synchronous(동기적) : 선언된 순서와 동일하게 실행됨
// asynchronous(비동기적) : 선언된 순서와 관계없이 한번에 실행됨 <- 이러한 성격을 non-blocking이라고 함