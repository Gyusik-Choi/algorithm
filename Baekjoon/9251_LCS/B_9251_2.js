const fs = require('fs')
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n')

const firstString = input[0].split('')
const secondString = input[1].split('')

const fLength = firstString.length
const sLength = secondString.length

let dp = new Array(fLength).fill(0).map(v => new Array(sLength).fill(0))

// 첫번째 문자열을 y축, 두번째 문자열을 x축으로 잡고
// y축의 첫번째 문자들과 x축 첫번째 문자 비교
const sTarget = secondString[0]
let sFlag = false
for (let i = 0; i < fLength; i++) {
    const firstStr = firstString[i]

    if (sTarget === firstStr || sFlag === true) {
        dp[i][0] = 1
        sFlag = true
    }
}

// x축의 첫번째 문자들과 y축 첫번째 문자 비교
const fTarget = firstString[0]
let fFlag = false
for (let j = 0; j < sLength; j++) {
    const secondStr = secondString[j]

    if (fTarget === secondStr || fFlag === true) {
        dp[0][j] = 1
        fFlag = true
    }
}

for (let i = 1; i < fLength; i++) {
    const first = firstString[i]
    for (let j = 1; j < sLength; j++) {
        const second = secondString[j]

        if (first === second) {
            dp[i][j] = Math.max(dp[i - 1][j], dp[i][j - 1]) + 1
        } else {
            dp[i][j] = Math.max(dp[i - 1][j], dp[i][j - 1])
        }
    }
}

console.log(dp[fLength - 1][sLength - 1])
