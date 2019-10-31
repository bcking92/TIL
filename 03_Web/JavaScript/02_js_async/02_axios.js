// 이 과정을 한번에 줄일 것이다
// const dogAPI = new XMLHttpRequest
// dogAPI.open()
// dogAPI.send()
// dogAPI.addEventListener()
const dogButton = document.querySelector('#dog')
const catButton = document.querySelector('#cat')
const dogURL = 'https://dog.ceo/api/breeds/image/random'
const catURL = 'https://api.thecatapi.com/v1/images/search'
// const result = axios.get(URL)
// // promise 객체 (resolved)

// // promise 객체를 까보기 위해 -> .then()
// result.then((result) => {
//     console.log(result.data.message)
// })


catButton.addEventListener('click', e =>{
    document.querySelector('#board').innerHTML = null
    for (let i=1; i<=9; i++){
    createPic(catURL)
    }
})

dogButton.addEventListener('click', e =>{
    document.querySelector('#board').innerHTML = null
    for (let i=1; i<=9; i++){
    createPic(dogURL)
    }
})

catButton.addEventListener('mouseover', e => {
    e.target.classList.value = "ml-3 btn btn-primary"
})

catButton.addEventListener('mouseout', e => {
    e.target.classList.value = "ml-3 btn btn-dark"
})

const createPic = URL => {
    const result = axios.get(URL)
    .then(result => {
        const myImg = document.createElement('img')
        if (URL === dogURL) {
            myImg.src = result.data.message
        } else {
            myImg.src = result.data[0].url
        }
        document.querySelector('#board').appendChild(myImg)
    })
}






// console.log(result.then())