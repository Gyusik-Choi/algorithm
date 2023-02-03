const inStack = function(stackInfo, y, x) {
    for (let i = 0; i < stackInfo.length; i++) {
        const [stackY, stackX] = stackInfo[i]

        if (stackY === y && stackX === x) {
            return true
        }
    }

    return false
}

const dfs = function(y, x) {
    let stack = [[y, x]]
    let cnt = 1

    let yDirection = [-1, 0, 1, 0]
    let xDirection = [0, 1, 0, -1]

    while (stack.length > 0) {
        const [yIdx, xIdx] = stack.pop()
        visited[yIdx][xIdx] = true

        for (let k = 0; k < 4; k++) {
            const yCoordinate = yDirection[k] + yIdx
            const xCoordinate = xDirection[k] + xIdx

            if (0 <= yCoordinate && yCoordinate < N && 0 <= xCoordinate && xCoordinate< N) {
                if (visited[yCoordinate][xCoordinate] === false && inStack(stack, yCoordinate, xCoordinate) === false) {
                    if (apartments[yCoordinate][xCoordinate] === 1) {
                        cnt += 1
                        stack.push([yCoordinate, xCoordinate])
                    }
                }
            }
        }
    }

    return cnt
}

const fs = require('fs')
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n')

const N = parseInt(input[0])
let apartments = []

for (let i = 1; i <= N; i++) {
    const aptInfo = input[i].split('').map(v => parseInt(v))
    apartments.push(aptInfo)
}

let numberOfApartmentComplex = 0
let numberOfApartmentPerComplex = []

let visited = new Array(N).fill(false).map(v => new Array(N).fill(false))

for (let i = 0; i < N; i++) {
    for (let j = 0; j < N; j++) {
        const apt = apartments[i][j]
        
        if (apt === 1 && visited[i][j] === false) {
            const nums = dfs(i, j)
            numberOfApartmentComplex += 1
            numberOfApartmentPerComplex.push(nums)
        }
    }
}

console.log(numberOfApartmentComplex)

numberOfApartmentPerComplex.sort((a, b) => a - b)
numberOfApartmentPerComplex.forEach((v, i) => console.log(v))