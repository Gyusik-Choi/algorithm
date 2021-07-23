const check = function(x) {
    for (let xCandidate = 0; xCandidate < x; xCandidate++) {
        if (vertical[x] === vertical[xCandidate]) {
            return false
        }

        if (Math.abs(vertical[x] - vertical[xCandidate]) === x - xCandidate) {
            return false
        }
    }
    return true
}

const nQueen = function(y) {
    if (y === N) {
        answer += 1
    } else {
        for (let x = 0; x < N; x++) {
            vertical[y] = x
            if (check(y)) {
                nQueen(y + 1)
            }
        }
    }
}

const fs = require('fs')
const input = fs.readFileSync('/dev/stdin').toString().trim()

const N = Number(input)
let answer = 0
let vertical = new Array(N).fill(0)

nQueen(0)
console.log(answer)
