const fs = require('fs')
const input = fs.readFileSync('/dev/stdin').toString().trim().split('')
const nums = input.map(v => Number(v))
nums.sort((a, b) => {
    return b - a
})
console.log(nums.join(''))