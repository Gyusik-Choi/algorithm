const bfs = function(y, x) {
    let visited = new Array(N).fill(0).map(v => new Array(M).fill(0))
    let queue = [[y, x]]
    visited[y][x] = 1

    let yDirection = [-1, 0, 1, 0]
    let xDirection = [0, 1, 0, -1]

    while (queue.length > 0) {
        const [yAxis, xAxis] = queue.shift()
        
        for (let j = 0; j < 4; j++) {
            const yWay = yAxis + yDirection[j]
            const xWay = xAxis + xDirection[j]
            
            if (0 <= yWay && yWay < N && 0 <= xWay && xWay < M) {
                if (yWay === N - 1 && xWay === M - 1) {
                    return visited[yAxis][xAxis] + 1
                }

                if (maze[yWay][xWay] === 1 && visited[yWay][xWay] === 0) {
                    queue.push([yWay, xWay])
                    visited[yWay][xWay] = visited[yAxis][xAxis] + 1
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
    const coordinate = input[i].split('').map(v => Number(v))
    maze.push(coordinate)  
}

const answer = bfs(0, 0)
console.log(answer)
