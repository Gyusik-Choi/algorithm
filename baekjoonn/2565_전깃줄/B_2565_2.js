const binarySearch = function(start, end, num) {
    if (start === end) {
        return end
    }

    const mid = Math.floor((start + end) / 2)

    if (num < dp[mid]) {
        return binarySearch(start, mid, num)
    }

    if (num > dp[mid]) {
        return binarySearch(mid + 1, end, num)
    }
}

const fs = require('fs')
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n')

const N = parseInt(input[0])
let electricCords = []

for (let i = 1; i <= N; i++) {
    const cord = input[i].split(' ').map(v => parseInt(v))
    electricCords.push(cord)
}

const sortedElectricCords = electricCords.sort((a, b) => {
    // if (a[0] === b[0]) {
    //     return a[1] - b[1]
    // }
    // 같은 위치에 두 개 이상의 전깃줄이 연결될 수 없다고 했으므로
    // 위의 조건은 없어도 된다
    return a[0] - b[0]
})

let dp = [sortedElectricCords[0][1]]
for (let i = 1; i < N; i++) {
    const [a, b] = sortedElectricCords[i]
    if (b > dp[dp.length - 1]) {
        dp.push(b)
    } else {
        const idx = binarySearch(0, dp.length - 1, b)
        dp[idx] = b
    }
}

console.log(N - dp.length)
