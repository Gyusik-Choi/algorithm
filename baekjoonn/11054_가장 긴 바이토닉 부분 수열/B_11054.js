const getLIS = function(arr) {
    let lis = new Array(N).fill(1)

    for (let i = 1; i < N; i++) {
        const target = arr[i]
        for (let j = 0; j < i; j++) {
            const candidate = arr[j]
            if (target > candidate) {
                lis[i] = Math.max(lis[j] + 1, lis[i])
            }
        }
    }

    return lis
}

const fs = require('fs')
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n')

const N = parseInt(input[0])
let sequence = input[1].split(' ').map(v => Number(v))
let reverseSequence = []
for (let i = sequence.length - 1; i > -1; i--) {
    const item = sequence[i]
    reverseSequence.push(item)
}

const sequenceLis = getLIS(sequence)
const reverseSequenceLis = getLIS(reverseSequence)

let sumLis = []
for (let i = 0; i < N; i++) {
    const sums = sequenceLis[i] + reverseSequenceLis[N - 1 - i] - 1
    sumLis.push(sums)
}

console.log(Math.max(...sumLis))