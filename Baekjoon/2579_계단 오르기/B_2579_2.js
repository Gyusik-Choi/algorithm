const fs = require('fs')
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n')

const N = parseInt(input[0])
let stairs = []
for (let i = 1; i <= N; i++) {
    const stair = parseInt(input[i])
    stairs.push(stair)
}

let dp = new Array(N).fill(0)
dp[0] = stairs[0]

if (N > 1) {
    dp[1] = Math.max(stairs[0], stairs[1], stairs[0] + stairs[1])
}

if (N > 2) {
    dp[2] = Math.max(stairs[0] + stairs[2], stairs[1] + stairs[2])
}

if (N >= 3) {
    for (let i = 3; i < N; i++) {
        dp[i] = Math.max(dp[i - 3] + stairs[i - 1] + stairs[i], dp[i - 2] + stairs[i])
    }
}

console.log(dp[N - 1])
