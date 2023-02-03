const dfsRecursion = function(coordinates, count) {
    let y_direction = [-1, 0, 1, 0]
    let x_direction = [0, 1, 0, -1]

    const [y, x] = coordinates
    visited[y][x] = true
    count += 1

    for (let k = 0; k < 4; k++) {
        y_axis = y_direction[k] + y
        x_axis = x_direction[k] + x

        if (0 <= y_axis && y_axis < N && 0 <= x_axis && x_axis < N) {
            if (apartments[y_axis][x_axis] === 1 && visited[y_axis][x_axis] === false) {
                count = dfsRecursion([y_axis, x_axis], count)
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
            const count = dfsRecursion([i, j], 0)
            counts.push(count)
        }
    }
}

console.log(answer)
counts.sort((a, b) => a - b)
counts.forEach((item) => console.log(item))
