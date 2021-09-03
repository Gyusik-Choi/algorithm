const fs = require('fs')
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n')

const N = parseInt(input[0])
let stairs = []

for (let i = 1; i <= N; i++) {
    const stair = parseInt(input[i])
    stairs.push(stair)
}

dp = new Array(N).fill(0)
if (N === 1) {
    dp[0] = stairs[0]
} else if (N === 2) {
    dp[0] = stairs[0]
    dp[1] = stairs[0] + stairs[1]
} else if (N === 3) {
    dp[0] = stairs[0]
    dp[1] = stairs[0] + stairs[1]
    dp[2] = Math.max(stairs[0], stairs[1]) + stairs[2]
} else {
    dp[0] = stairs[0]
    dp[1] = stairs[0] + stairs[1]
    dp[2] = Math.max(stairs[0], stairs[1]) + stairs[2]
    
    for (let i = 3; i < N; i++) {
        dp[i] = Math.max(dp[i - 3] + stairs[i - 1], dp[i - 2]) + stairs[i]
    }
}

console.log(dp[N - 1])
