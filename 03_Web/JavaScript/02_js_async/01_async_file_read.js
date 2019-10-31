const fs = require('fs')

console.log('파일 읽기 전')

// fs.readFile('me2.json', (err, data) => {
//     console.log('파일 탐지')
//     setTimeout(() => {
//         console.log(JSON.parse(data))
//     }
//     , 10000)
// })

// 비동기적함수( , function) <- 비동기적함수가 
// 언제 끝날지 몰라 그래서 그 이후에 이걸(function) 실행해 줬으면 좋겠어

const content = fs.readFileSync('me2.json')

console.log('읽기 종료')

console.log(JSON.parse(content))

console.log('끝')