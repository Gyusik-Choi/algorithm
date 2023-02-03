const fs = require('fs')
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n')

const N = parseInt(input[0])
let wineGlasses = []

for (let i = 1; i <= N; i++) {
    const wineGlass = parseInt(input[i])
    wineGlasses.push(wineGlass)
}

dp = new Array(N).fill(0)

if (N < 2) {
    dp[0] = wineGlasses[0]
} else if (N < 3) {
    dp[0] = wineGlasses[0]
    dp[1] = wineGlasses[0] + wineGlasses[1]
} else if (N < 4) {
    dp[0] = wineGlasses[0]
    dp[1] = wineGlasses[0] + wineGlasses[1]
    dp[2] = Math.max(wineGlasses[0] + wineGlasses[1], wineGlasses[0] + wineGlasses[2], wineGlasses[1] + wineGlasses[2])
} else {
    dp[0] = wineGlasses[0]
    dp[1] = wineGlasses[0] + wineGlasses[1]
    dp[2] = Math.max(wineGlasses[0] + wineGlasses[1], wineGlasses[0] + wineGlasses[2], wineGlasses[1] + wineGlasses[2])
    
    // 이전의 값이 더 클 수도 있다
    // 이전의 값(dp[i - 1]), dp[i - 2] + wineGlasses[i], dp[i - 3] + wineGlasses[i - 1] + wineGlasses[i] 
    for (let i = 3; i < N; i++) {
        dp[i] = Math.max(dp[i - 1], dp[i - 2] + wineGlasses[i], dp[i - 3] + wineGlasses[i - 1] + wineGlasses[i])
    }
}

// 인덱스 주의
console.log(dp[N - 1])