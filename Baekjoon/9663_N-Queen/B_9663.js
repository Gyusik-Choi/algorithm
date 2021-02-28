const nQueen = function(y) {
    if (y === N) {
        cnt++
        return
    } else {
        for (let x = 0; x < N; x++) {
            if (vertical[x] === 0 && diagonal1[N + y - x - 1] === 0 && diagonal2[y + x] === 0) {
                vertical[x] = 1
                diagonal1[N + y - x - 1] = 1
                diagonal2[y + x] = 1
                nQueen(y + 1)
                vertical[x] = 0
                diagonal1[N + y - x - 1] = 0
                diagonal2[y + x] = 0
            }
        }
    }
}

const fs = require('fs')
const N = parseInt(fs.readFileSync('/dev/stdin'))

let vertical = new Array(N).fill(0)
let diagonal1 = new Array(2 * N - 1).fill(0)
let diagonal2 = new Array(2 * N - 1).fill(0)

let cnt = 0
nQueen(0)
console.log(cnt)