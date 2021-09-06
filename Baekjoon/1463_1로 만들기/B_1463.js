const fs = require('fs')
const input = fs.readFileSync('/dev/stdin').toString()

const N = parseInt(input)

let dp = new Array(N + 1).fill(0)

if (N < 2) {
    
} else if (N < 3) {
    dp[2] = 1
} else if (N < 4) {
    dp[2] = 1
    dp[3] = 1
} else {
    dp[2] = 1
    dp[3] = 1
    for (let i = 4; i <= N; i++) {
        let min_num = dp[i - 1]
        
        if (i % 2 === 0) {
            min_num = Math.min(min_num, dp[i / 2])
        }

        if (i % 3 === 0) {
            min_num = Math.min(min_num, dp[i / 3])
        }

        dp[i] = min_num + 1
    }
}

console.log(dp[N])
