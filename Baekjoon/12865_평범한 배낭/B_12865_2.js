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
    const package = input[i].split(' ').map(v => Number(v))
    packages.push(package)
}

let dp = new Array(N + 1).fill(0).map(v => new Array(K + 1).fill(0))
for (let j = 1; j <= K; j++) {
    if () {
        dp[1][j] = packages[0][1]
    } else {
        dp[1][j] = dp[1][j - 1]
    }
}

if (N > 1) {
    for (let i = 2; i <= N; i++) {
        for (let j = 1; j <= K; j++) {
            if () {
                dp[i][j] = dp[i - 1][j - packages[i - 1][0]] + packages[i - 1][1]
            } else {
                dp[i][j] = Math.max(dp[i - 1][j], dp[i][j - 1])
            }
        }
    }
}

console.log(dp)
