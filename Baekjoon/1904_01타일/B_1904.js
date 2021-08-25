const fs = require('fs')
const input = fs.readFileSync('/dev/stdin').toString()
const N = Number(input)

let answers = new Array(1000001).fill(0)
answers[0] = 1
answers[1] = 1
answers[2] = 2

for (let i = 3; i <= 1000000; i++) {
    answers[i] = (answers[i - 1] + answers[i - 2]) % 15746
}

console.log(answers[N])