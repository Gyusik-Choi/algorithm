const getFibonacciValue = function(n) {
    while (n <= 100) {
        arr[n] = arr[n - 3] + arr[n - 2]
        n += 1
    }
}

const fs = require('fs')
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n')

const T = parseInt(input[0])

let arr = new Array(101).fill(4)
getFibonacciValue(1)

for (let i = 1; i <= T; i++) {
    const N = parseInt(input[i])
    console.log(arr[N])
}