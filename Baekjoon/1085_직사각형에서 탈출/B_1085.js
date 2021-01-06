const fs = require('fs')
const input = fs.readFileSync('/dev/stdin').toString().trim().split(' ')
let arr = input.map(v => Number(v))

let minSubtraction = 1000
for (let i = 0; i < 2; i++) {
    let subtraction1 = arr[i]
    let subtraction2 = arr[i + 2] - arr[i]
    let subtraction3 = Math.min(subtraction1, subtraction2)
    minSubtraction = Math.min(minSubtraction, subtraction3)
}
console.log(minSubtraction)
