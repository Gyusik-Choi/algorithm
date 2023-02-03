const fs = require('fs')
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n')

const NK = input[0].split(' ').map(v => Number(v))
const N = NK[0]
const K = NK[1]

let weightAndValues = []
for (let i = 1; i <= N; i++) {
    const weightAndValue = input[i].split(' ').map(v => Number(v))
    weightAndValues.push(weightAndValue)
}

let dp = new Array(N + 1).fill(0).map(v => new Array(K + 1).fill(0))

for (let i = 1; i <= N; i++) {
    for (let j = 1; j <= K; j++) {
        const weight = weightAndValues[i - 1][0]
        const value = weightAndValues[i - 1][1]

        if (weight <= j) {
            dp[i][j] = Math.max(dp[i - 1][j], dp[i - 1][j - weight] + value)
        } else {
            dp[i][j] = dp[i - 1][j]
        }
    }
}

console.log(dp[N][K])
