const fs = require('fs')
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n')

const T = parseInt(input[0])
let idx = 1

for (let i = 0; i < T; i++) {
    let NM = input[idx].split(' ').map(v => parseInt(v))
    const N = NM[0]
    const M = NM[1]

    idx += M + 1
    console.log(N - 1)
}
