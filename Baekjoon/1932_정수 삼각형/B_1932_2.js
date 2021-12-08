const fs = require('fs')
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n')

const n = parseInt(input[0])
let triangle = []

for (let i = 1; i <= n; i++) {
    const nums = input[i].split(' ').map(v => Number(v))
    triangle.push(nums)
}

for (let i = 1; i < n; i++) {
    const leng = triangle[i].length
    for (let j = 0; j < leng; j++) {
        if (j === 0) {
            triangle[i][j] += triangle[i - 1][j]
        } else if (j === leng - 1) {
            triangle[i][j] += triangle[i - 1][j - 1]
        } else {
            triangle[i][j] += Math.max(triangle[i - 1][j - 1], triangle[i - 1][j])
        }
    }
}

console.log(Math.max(...triangle[n - 1]))
