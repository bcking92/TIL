// python dictionary와 다르게 js object는 키를 string이 아니라 변수명 처럼 써도 작동한다.
const fs = require('fs')


const me = {
    name: 'kim',
    // sleep: function () {
    //     console.log('쿨쿨')
    // },
    appleProduct: {
        macBook: '2018pro',
        iPad: '2018pro',  
    },
}

console.log(me)
console.log(me.name)
console.log(me['name'])
// console.log(me.sleep)
// console.log(me.sleep())
console.log(me.appleProduct.macBook)

// JSON(JavaScript Object Notation)

// object를 JSON으로 만들기
const meJSON = JSON.stringify(me)
console.log(typeof meJSON)
console.log(meJSON)

// 현재 폴더에 넣을때는 경로 설정 필요 X
fs.writeFile('me.json', meJSON, err => {})
fs.writeFileSync('me2.json', meJSON)

// JSON을 object로 바꾸기
const meObject = JSON.parse(meJSON)
console.log(typeof meObject)
console.log(meObject)