const fs = require('fs')
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n')

const n = parseInt(input[0])
let wines = []
for (let i = 1; i <= n; i++) {
    const wine = parseInt(input[i])
    wines.push(wine)
}

let dp = new Array(n).fill(0)
dp[0] = wines[0]

if (n > 1) {
    dp[1] = wines[0] + wines[1]
}

if (n > 2) {
    dp[2] = Math.max(wines[0] + wines[1], wines[0] + wines[2], wines[1] + wines[2])
}

if (n > 3) {
    for (let j = 3; j < n; j++) {
        dp[j] = Math.max(dp[j - 3] + wines[j - 1] + wines[j], dp[j - 2] + wines[j], dp[j - 1])
    }
}

console.log(Math.max(...dp))
