const fs = require('fs')
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n')

const n = Number(input[0])
const sequence = input[1].split(' ').map(v => Number(v))

let dp = new Array(n).fill(0)
dp[0] = sequence[0]

if (n > 1) {
    for (let i = 1; i < n; i++) {
        const number = sequence[i]

        dp[i] = Math.max(dp[i - 1] + number, number)
    }
}

const answer = Math.max(...dp)
console.log(answer)
