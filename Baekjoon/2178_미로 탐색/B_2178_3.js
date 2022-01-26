const bfs = function(yStart, xStart, num) {
    let queue = [[yStart, xStart, num]]
    
    let visited = new Array(N).fill(false).map(v => new Array(M).fill(false))
    visited[0][0] = true
    
    while (queue.length > 0) {
        const [y, x, minNum] = queue.shift()

        const yDirection = [-1, 0, 1, 0]
        const xDirection = [0, 1, 0, -1]
    
        for (let i = 0; i < 4; i++) {
            const yIdx = y + yDirection[i]
            const xIdx = x + xDirection[i]
            
            if (yIdx === N - 1 && xIdx === M - 1) {
                return minNum + 1
            }
    
            if (0 <= yIdx && yIdx < N && 0 <= xIdx && xIdx < M) {
                if (maze[yIdx][xIdx] === 1 && visited[yIdx][xIdx] === false) {
                    visited[yIdx][xIdx] = true
                    queue.push([yIdx, xIdx, minNum + 1])
                }
            }
        }
    }
}

const fs = require('fs')
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n')

const [N, M] = input[0].split(' ').map(v => Number(v))
let maze = []

for (let i = 1; i <= N; i++) {
    const mazeInfo = input[i].split('').map(v => Number(v))
    maze.push(mazeInfo)
}

const answer = bfs(0, 0, 1)
console.log(answer)
