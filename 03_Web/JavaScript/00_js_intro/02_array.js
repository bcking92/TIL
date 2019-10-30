const nums = [1, 2, 3, 4]

console.log(nums[0])
console.log(nums[nums.length - 1])

// method는 원본을 바꾼다.
console.log(nums.reverse())
console.log(nums)

nums.push(0)
console.log(nums)

nums.pop()
console.log(nums)

// unshift, shift, includes, indexOf
nums.unshift(5)
console.log(nums)

nums.shift()
console.log(nums)

// nums[-1] = 1
console.log(nums)

console.log(nums.includes(0))
console.log(nums.includes(4))

console.log(nums.indexOf(1))

for (let num of nums) {
    console.log(num)
}

console.log('-------------------')

// 이터러블.forEach(함수)
// -> 이터러블을 수행하며 함수를 각각의 요소에 실행
nums.forEach(function(num) {
    console.log(num + num)
})

// nums 안의 요소를 각각 제곱하시오
// nums.pop()
nums.forEach(function(num) {
    nums[nums.indexOf(num)] = num ** 2
})

console.log(nums)

const newNums = nums.map(function(num) {
    return num * num
})

console.log(newNums)