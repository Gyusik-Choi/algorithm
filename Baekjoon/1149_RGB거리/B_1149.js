const fs = require('fs')
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n')

const N = Number(input[0])

let rgbValues = []
for (let i = 1; i <= N; i++) {
    const values = input[i].split(' ').map(v => Number(v))
    rgbValues.push(values)
}

dp = new Array(N).fill(Infinity).map(v => new Array(N).fill(Infinity))

dp[0][0] = rgbValues[0][0]
dp[0][1] = rgbValues[0][1]
dp[0][2] = rgbValues[0][2]

for (let i = 1; i < N; i++) {
    for (let j = 0; j < 3; j++) {
        for (let k = 0; k < 3; k++) {
            if (j != k) {
                if (dp[i - 1][j] + rgbValues[i][k] < dp[i][k]) {
                    dp[i][k] = dp[i - 1][j] + rgbValues[i][k]
                }
            }
        }
    }
}

console.log(Math.min(dp[N - 1][0], dp[N - 1][1], dp[N - 1][2]))