const binarySearch = function(start, end, num) {
    const mid = Math.floor((start + end) / 2)

    // 탈출 조건이 핵심
    // if (start === mid) {
    // 위의 조건은 num이 가장 작을 경우를 고려하지 못한다
    if (start === end) {
        return end
    }

    if (dp[mid] > num) {
        return binarySearch(start, mid, num)
    } else {
        if (dp[mid] === num) {
            return mid
        }
        return binarySearch(mid + 1, end, num)
    }
}

const fs = require('fs')
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n')

const N = parseInt(input[0])
const sequence = input[1].split(' ').map(v => parseInt(v))

let dp = [sequence[0]]

for (let i = 1; i < N; i++) {
    const number = sequence[i]

    if (number > dp[dp.length - 1]) {
        dp.push(number)
    } else {
        const idx = binarySearch(0, dp.length - 1, number)
        dp[idx] = number
    }
}

console.log(dp.length)
