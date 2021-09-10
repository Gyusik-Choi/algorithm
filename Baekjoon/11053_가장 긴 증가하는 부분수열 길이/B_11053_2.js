const binarySearch = function(start, end, item) {
    if (start >= end) {
        return end
    }

    let mid = Math.floor((start + end) / 2)
    if (dp[mid] > item) {
        return binarySearch(start, mid, item)
    } else {
        if (dp[mid] === item) {
            return mid
        } else {
            return binarySearch(mid + 1, end, item)
        }
    }
}

const fs = require('fs')
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n')

const N = Number(input[0])
const sequence = input[1].split(' ').map(v => Number(v))

let dp = [sequence[0]]
for (let i = 1; i < N; i++) {
    const target = sequence[i]
    if (dp[dp.length - 1] < target) {
        dp.push(target)
    } else {
        // 같은 경우는 제외
        if (dp[dp.length - 1] > target) {
            const idx = binarySearch(0, dp.length - 1, target)
            dp[idx] = target
        }
    }
}

console.log(dp.length)