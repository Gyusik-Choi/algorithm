const w = function(a, b, c) {
    if (a <= 0 || b <= 0 || c <= 0) {
        return 1
    }

    if (a <= 20 && b <= 20 && c <= 20) {
        if (dp[a][b][c] !== 0) {
            return dp[a][b][c]
        }
    }

    if (a > 20 || b > 20 || c > 20) {
        dp[20][20][20] = w(20, 20, 20)
        return dp[20][20][20]
    }

    if (a < b && b < c) {
        dp[a][b][c] = w(a, b, c - 1) + w(a, b - 1, c - 1) - w(a, b - 1, c)
        return dp[a][b][c]
    }

    dp[a][b][c] = w(a - 1, b, c) + w(a - 1, b - 1, c) + w(a - 1, b, c - 1) - w(a - 1, b - 1, c - 1)
    return dp[a][b][c]
}

const fs = require('fs')
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n')

let numbers = []
for (let i = 0; i < input.length; i++) {
    const numberArray = input[i].split(' ').map(v => Number(v))
    numbers.push(numberArray)
}

let dp = new Array(21).fill(0).map(v => new Array(21).fill(0).map(v => new Array(21).fill(0)))

numbers.forEach((v, i) => {
    const A = v[0]
    const B = v[1]
    const C = v[2]
    answer = w(A, B, C)
    console.log(`w(${A}, ${B}, ${C}) = ${answer}`)
})