const fs = require('fs')
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n')

const T = Number(input[0])

let idx = 1
for (let i = 0; i < T; i++) {

    const dfsRecursion = function(start) {
        
    }

    const [M, N, K] = input[idx].split(' ').map(v => Number(v))

    let cabbageField = new Array(N + 1).fill(0).map(v => new Array())
    for (let j = idx + 1; j < idx + 1 + K; j++) {
        const [x, y] = input[j].split(' ').map(v => Number(v))
        cabbageField[y].push(x)

        for (let k = 0; k < N; k++) {
            for (let l = 0; l < M; l++) {
                if (cabbageField[k][l] === 1) {
                    dfsRecursion([k, l])
                }
            }
        }
    }
}