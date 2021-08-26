const fs = require('fs')
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n')

const T = Number(input[0])
let numbers = [1, 1, 1, 2, 2, 3]
for (let i = 6; i < 100; i++) {
    const number = numbers[i - 3] + numbers[i - 2]
    numbers.push(number)
}

for (let i = 1; i <= T; i++) {
    const N = Number(input[i])
    console.log(numbers[N - 1])
}