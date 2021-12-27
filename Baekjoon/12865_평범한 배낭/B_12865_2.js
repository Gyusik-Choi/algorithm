const fs = require('fs')
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n')

// 동적계획법 문제다
// 문제의 아이디어는 우선 최대 무게와 주어진 물건 갯수를 바탕으로 2차원 배열을 만들어서
// 물건 하나를 했을때 최대 무게 - 물건 무게를 충족하는 경우에만 물건을 더 담는 방식을 활용해보려고 한다

const fs = require('fs')
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n')

const [N, K] = input[0].split(' ').map(v => Number(v))
let packages = []

for (let i = 1; i <= N; i++) {
    const [weight, value] = packages[i - 1]

    for (let j = 1; j <= K; j++) {
        if (weight <= j) {
            dp[i][j] = Math.max(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - weight] + value)
        } else {
            dp[i][j] = Math.max(dp[i - 1][j], dp[i][j - 1])
        }
    }
}

console.log(dp[N][K])
