const fs = require('fs')
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n')

const T = parseInt(input[0])
let memoization = new Array(41).fill(0)
memoization[1] = 1
memoization[2] = 1

for (let i = 3; i <= 40; i++) {
    memoization[i] = memoization[i - 2] + memoization[i - 1]
}

for (let i = 1; i <= T; i++) {
    const N = parseInt(input[i])

    if (N === 0) {
        console.log(1, 0)
    } else if (N === 1) {
        console.log(0, 1)
    } else if (N === 2) {
        console.log(1, 1)
    } else {
        console.log(memoization[N - 3] + memoization[N - 2], memoization[N - 2] + memoization[N - 1])
    }
}
