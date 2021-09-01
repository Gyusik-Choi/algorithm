const fs = require('fs')
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n')

const N = parseInt(input[0])
let triangleValues = []

let dp = []
for (let i = 1; i <= N; i++) {
    const triangle = input[i].split(' ').map(v => parseInt(v))
    triangleValues.push(triangle)

    const dpValues = new Array(i).fill(0)
    dp.push(dpValues)
}


dp[0][0] = triangleValues[0][0]

for (let i = 1; i < N; i++) {
    for (let j = 0; j < triangleValues[i].length; j++) {
        if (j === 0) {
            dp[i][j] = dp[i - 1][j] + triangleValues[i][j]
        } else if (j === triangleValues[i].length - 1) {
            dp[i][j] = dp[i - 1][j - 1] + triangleValues[i][j]
        } else {
            dp[i][j] = Math.max(dp[i - 1][j - 1], dp[i - 1][j]) + triangleValues[i][j]
        }
    }
}

let maxVal = 0
for (let i = 0; i < dp[N - 1].length; i++) {
    const candidateMaxVal = dp[N - 1][i]
    if (maxVal < candidateMaxVal) {
        maxVal = candidateMaxVal
    }
}

console.log(maxVal)
