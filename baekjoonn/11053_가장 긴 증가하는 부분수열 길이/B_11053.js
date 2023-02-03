const fs = require('fs')
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n')

const N = Number(input[0])
const sequence = input[1].split(' ').map(v => Number(v))

let lis = new Array(N).fill(1)

for (let i = N - 2; i > -1; i--) {
    const target = sequence[i]
    for (let j = N - 1; j > i; j--) {
        const candidate = sequence[j]
        if (target < candidate) {
            lis[i] = Math.max(lis[j] + 1, lis[i])
        }
    }
}

console.log(Math.max(...lis))