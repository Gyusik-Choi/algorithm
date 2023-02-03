const fs = require('fs')
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n')

const N = parseInt(input[0])
const sequence = input[1].split(' ').map(v => parseInt(v))

let dpAscent = new Array(N).fill(1)
let dpDescent = new Array(N).fill(1)

let answer = 1
if (N > 1) {
    for (let i = 1; i < N; i++) {
        const target = sequence[i]
        let maxLength = 1
        for (let j = 0; j < i; j++) {
            if (target > sequence[j]) {
                maxLength = Math.max(maxLength, dpAscent[j] + 1)
            }
        }

        dpAscent[i] = maxLength
    }

    for (let i = N - 2; i > -1; i--) {
        const target = sequence[i]
        let maxLength = 1
        for (let j = i + 1; j < N; j++) {
            if (target > sequence[j]) {
                maxLength = Math.max(maxLength, dpDescent[j] + 1)
            }
        }

        dpDescent[i] = maxLength
        answer = Math.max(answer, dpAscent[i] + dpDescent[i] - 1)
    }
}

console.log(answer)
