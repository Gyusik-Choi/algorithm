const fs = require('fs')
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n')

const N = Number(input[0])

let rgbValues = []
for (let i = 1; i <= N; i++) {
    const values = input[i].split(' ').map(v => Number(v))
    rgbValues.push(values)
}

dp = new Array(N).fill(0).map(v => new Array(N).fill(0))

dp[0][0] = rgbValues[0][0]
dp[0][1] = rgbValues[0][1]
dp[0][2] = rgbValues[0][2]

for (let i = 1; i < N; i++) {
    dp[i][0] = Math.min(dp[i - 1][1], dp[i - 1][2]) + rgbValues[i][0]
    dp[i][1] = Math.min(dp[i - 1][0], dp[i - 1][2]) + rgbValues[i][1]
    dp[i][2] = Math.min(dp[i - 1][0], dp[i - 1][1]) + rgbValues[i][2]
}

console.log(Math.min(dp[N - 1][0], dp[N - 1][1], dp[N - 1][2]))