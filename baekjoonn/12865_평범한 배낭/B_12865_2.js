const fs = require('fs')
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n')

// 동적계획법 문제다
// 문제의 아이디어는 우선 최대 무게와 주어진 물건 갯수를 바탕으로 2차원 배열을 만들어서
// 물건 하나를 최대 무게 - 물건 무게를 충족하는 경우에만 더 담는 방식을 활용해보려고 한다

const fs = require('fs')
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n')

const [N, K] = input[0].split(' ').map(v => Number(v))
let packages = []

for (let i = 1; i <= N; i++) {
    const [weight, value] = packages[i - 1]

    for (let j = 1; j <= K; j++) {
        if (weight <= j) {
            dp[i][j] = Math.max(dp[i - 1][j], dp[i - 1][j - weight] + value)
            // dp[i][j] = Math.max(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - weight] + value)
            // dp[i][j - 1]를 고려할 필요가 없다
            // 물건 하나를 더 담을 수 있는 경우이므로 dp[i][j - 1]은 더 담는 것과는 관계가 없다
            // dp[i - 1][j]는 담지 않고, dp[i - 1][j - weight] + value는 하나 더 담는 경우다
            // 이 둘의 비교 외에 dp[i][j - 1]은 불필요한 조건이다
        } else {
            dp[i][j] = dp[i - 1][j]
            // dp[i][j] = Math.max(dp[i - 1][j], dp[i][j - 1])
            // 위처럼 마찬가지로 dp[i][j - 1]을 고려할 필요가 없다
            // 물건 하나를 더 담을 수 없는 경우라 이전의 경우의 값을 그대로 가져와야 한다
            // 여기서 이전의 경우라는건 이전까지 물건을 담았던 상태이므로 dp[i - 1][j]를 나타내며
            // dp[i][j - 1]은 현재 물건의 무게가 1만큼 더 가벼운 경우를 다루므로 적절하지 않다
        }
    }
}

console.log(dp[N][K])
