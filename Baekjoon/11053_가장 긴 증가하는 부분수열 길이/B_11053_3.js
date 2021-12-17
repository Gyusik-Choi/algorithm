const fs = require('fs')
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n')

const N = parseInt(input[0])
const sequence = input[1].split(' ').map(v => parseInt(v))

let sequenceLength = new Array(N).fill(1)

for (let i = 1; i < N; i++) {
    const target = sequence[i]
    let maxLength = sequenceLength[i]
    for (let j = 0; j < i; j++) {
        if (target > sequence[j]) {
            maxLength = Math.max(sequenceLength[j] + 1, maxLength)
        }
    }
    sequenceLength[i] = maxLength
}

console.log(Math.max(...sequenceLength))