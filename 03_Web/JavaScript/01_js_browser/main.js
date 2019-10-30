/* 1. <input> 태그 안의 값을 잡는다. */
const inputArea = document.querySelector('#js-userinput')
const button = document.querySelector('#js-go')
const resultArea = document.querySelector('#result-area')
const myButton = document.querySelector('#my-button')

button.addEventListener('click', e => {
    GiphyGiphyYeYe()
})

inputArea.addEventListener('keydown', e => {
    if (e.keyCode === 13) {
        GiphyGiphyYeYe()
    }
})
/* 2. Giphy API 를 통해 data 를 받아서 가공한다. */

const GiphyGiphyYeYe = () => {
    let keyword = inputArea.value
    const API_KEY = ''
    resultArea.innerHTML = ''
    const URL = `http://api.giphy.com/v1/gifs/search?q=${keyword}&api_key=${API_KEY}`
    const GiphyAPICall = new XMLHttpRequest()
    GiphyAPICall.open('GET', URL)
    GiphyAPICall.send()
    GiphyAPICall.addEventListener('load', e => {
        const parsedData = JSON.parse(e.target.response)
        // console.log(parsedData)
        pushToDOM(parsedData.data)
        })
    }
// GiphyAPICall.open('HTTP method', 'ULR')


/* 3. GIF 파일들을 index.html(DOM)에 밀어 넣어서 보여준다. */
const pushToDOM = data => {
    data.forEach(element => {
        resultArea.innerHTML += `<img src="${element.images.original.url}" class='container-image'>` 
    // const elem = document.createElement('img')
    // elem.src = element.images.original.url
    // resultArea.appendChild(elem)
    });
}