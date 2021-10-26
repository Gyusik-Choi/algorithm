const fs = require('fs')
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n')

const T = Number(input[0])

let idx = 1
for (let i = 0; i < T; i++) {

    const dfsRecursion = function(start) {
        const [yAxis, xAxis] = start
        
        const yCoordinate = [-1, 0, 1, 0]
        const xCoordinate = [0, 1, 0, -1]
    
        for (let m = 0; m < 4; m++) {
            const yDirection = yAxis + yCoordinate[m]
            const xDirection = xAxis + xCoordinate[m]
    
            if (0 <= yDirection && yDirection < N && 0 <= xDirection && xDirection < M) {
                if (cabbageField[yDirection][xDirection] === 1) {
                    cabbageField[yDirection][xDirection] = 0
                    dfsRecursion([yDirection, xDirection])
                }
            }
        }
    }

    const [M, N, K] = input[idx].split(' ').map(v => Number(v))

    let answer = 0
    let cabbageField = new Array(N + 1).fill(0).map(v => new Array(M + 1).fill(0))
    for (let j = idx + 1; j < idx + 1 + K; j++) {
        const [x, y] = input[j].split(' ').map(v => Number(v))
        cabbageField[y][x] = 1
    }

    for (let k = 0; k < N; k++) {
        for (let l = 0; l < M; l++) {
            if (cabbageField[k][l] === 1) {
                dfsRecursion([k, l])
                answer += 1
            }
        }
    }

    console.log(answer)
    idx += 1 + K
}