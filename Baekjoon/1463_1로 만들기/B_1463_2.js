const fs = require('fs')
const N = parseInt(fs.readFileSync('/dev/stdin').toString().trim())

let dp = new Array(N + 1).fill(0)
dp[1] = 0

if (N > 1) {
    dp[2] = 1
}

if (N > 2) {
    dp[3] = 1
}

if (N > 3) {
    for (let i = 4; i <= N; i++) {
        if (i % 3 === 0 && i % 2 === 0) {
            dp[i] = Math.min(dp[i / 3], dp[i / 2], dp[i - 1]) + 1
        } else if (i % 3 === 0) {
            dp[i] = Math.min(dp[i / 3], dp[i - 1]) + 1
        } else if (i % 2 === 0) {
            dp[i] = Math.min(dp[i / 2], dp[i - 1]) + 1
        } else {
            dp[i] = dp[i - 1] + 1
        }
    }
}

console.log(dp[N])
