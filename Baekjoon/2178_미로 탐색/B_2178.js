const bfs = function(y, x) {
    let visited = new Array(N).fill(0).map(v => new Array(M).fill(0))
    let queue = [[y, x, 1]]

    let yDirection = [-1, 0, 1, 0]
    let xDirection = [0, 1, 0, -1]

    while (queue.length > 0) {
        const [yAxis, xAxis, cnt] = queue.shift()
        visited[yAxis][xAxis] = 1

        for (let j = 0; j < 4; j++) {
            const yWay = yAxis + yDirection[j]
            const xWay = xAxis + xDirection[j]

            if (yWay === N - 1 && xWay === M - 1) {
                return cnt + 1
            }

            if (maze[yWay][xWay] === 1 && visited[yWay][xWay] === 0) {
                queue.push([yWay, xWay, cnt + 1])
            }
        }
    }

}

const fs = require('fs')
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n')

const [N, M] = input[0].split(' ').map(v => Number(v))
let maze = []
for (let i = 0; i < N; i++) {
    const coordinate = input[i].split('').map(v => Number(v))
    maze.push(coordinate)  
}

const answer = bfs(N - 1, M - 1)
console.log(answer)
