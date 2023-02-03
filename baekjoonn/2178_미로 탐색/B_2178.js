const isInQueue = function(q, candidate) {
    const [yCandidate, xCandidate, cntCandidate] = candidate
    for (let k = 0; k < q.length; k++) {
        const [yQ, xQ, cntQ] = q[k]

        if (yCandidate === yQ && xCandidate === xQ && cntCandidate === cntQ) {
            return true
        }
    }

    return false
}

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

            if (0 <= yWay && yWay < N && 0 <= xWay && xWay < M) {
                if (yWay === N - 1 && xWay === M - 1) {
                    return cnt + 1
                }

                if (maze[yWay][xWay] === 1 && visited[yWay][xWay] === 0 && isInQueue(queue, [yWay, xWay, cnt + 1]) === false) {
                    queue.push([yWay, xWay, cnt + 1])
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
