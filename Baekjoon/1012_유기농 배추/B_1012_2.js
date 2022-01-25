const fs = require('fs')
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n')

const T = parseInt(input[0])
let idx = 1
for (let i = 0; i < T; i++) {
    const dfsRecursion = function(y, x, v) {
        const yDirection = [-1, 0, 1, 0]
        const xDirection = [0, 1, 0, -1]
    
        for (let i = 0; i < 4; i++) {
            const yIdx = y + yDirection[i]
            const xIdx = x + xDirection[i]
    
            if (0 <= yIdx && yIdx < M && 0 <= xIdx && xIdx < N) {
                if (cabbageField[yIdx][xIdx] === 1 && v[yIdx][xIdx] === false) {
                    v[yIdx][xIdx] = true
                    dfsRecursion(yIdx, xIdx, v)
                }
            }
        }
    }

    const [M, N, K] = input[idx].split(' ').map(v => parseInt(v))
    
    let cabbageField = new Array(M).fill(0).map(v => new Array(N).fill(0))
    for (let j = idx + 1; j < idx + 1 + K; j++) {
        const [Y, X] = input[j].split(' ').map(v => parseInt(v))
        cabbageField[Y][X] = 1
    }
    
    let visited = new Array(M).fill(false).map(v => new Array(N).fill(false))
    let answer = 0

    for (let k = 0; k < M; k++) {
        for (let l = 0; l < N; l++) {
            if (cabbageField[k][l] === 1 && visited[k][l] === false) {
                visited[k][l] = true
                answer += 1
                dfsRecursion(k, l, visited)
            }
        }
    }

    console.log(answer)
    idx += K + 1
}
