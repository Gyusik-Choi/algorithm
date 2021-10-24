const findNumber = function(queue, numbers) {
    for (let i = 0; i < queue.length; i++) {
        if (queue[i].join(' ') === numbers.join(' ')) {
            return true
        }
    }
    // queue.forEach((q) => {
    //     if (q.join(' ') === numbers.join(' ')) {
    //         return true
    //     }
    // })
    return false
}

const bfs = function(y, x) {
    let count = 0
    let queue = [[y, x]]

    let y_direction = [-1, 0, 1, 0]
    let x_direction = [0, 1, 0, -1]

    while (queue.length > 0) {
        const [y_axis, x_axis] = queue.shift()
        visited[y_axis][x_axis] = true
        count += 1
        
        for (let k = 0; k < 4; k++) {
            const y_coordinate = y_axis + y_direction[k]
            const x_coordinate = x_axis + x_direction[k]

            if (0 <= y_coordinate && y_coordinate < N && 0 <= x_coordinate && x_coordinate < N) {
                if (apartments[y_coordinate][x_coordinate] === 1 && visited[y_coordinate][x_coordinate] === false) {
                    if (findNumber(queue, [y_coordinate, x_coordinate]) === false) {
                        queue.push([y_coordinate, x_coordinate])
                    }
                }
            }
        }
    }
    
    return count
}

const fs = require('fs')
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n')

const N = Number(input[0])
let apartments = []
for (let i = 1; i <= N; i++) {
    const apartmentInfo = input[i].split('').map(v => Number(v))
    apartments.push(apartmentInfo)
}

let visited = new Array(N).fill(false).map(v => new Array(N).fill(false))

let answer = 0
let counts = []
for (let i = 0; i < N; i++) {
    for (let j = 0; j < N; j++) {
        if (apartments[i][j] === 1 && visited[i][j] === false) {
            answer += 1
            const count = bfs(i, j)
            counts.push(count)
        }
    }
}

console.log(answer)
counts.sort((a, b) => a - b)
counts.forEach((item) => console.log(item))
