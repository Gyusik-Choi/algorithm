const fs = require('fs')
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n')

const N = Number(input[0])
const numbers = input[1].split(' ').map(v => Number(v))

let dp = new Array(N).fill(0)
dp[0] = numbers[0]

let maxNum = dp[0]
for (let i = 1; i < N; i++) {
    dp[i] = Math.max(dp[i - 1] + numbers[i], numbers[i])

    maxNum = Math.max(maxNum, dp[i])
}
console.log(maxNum)