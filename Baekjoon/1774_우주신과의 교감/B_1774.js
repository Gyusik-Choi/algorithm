// 이미 연결된 우주신들의 union 연산을 수행한 후에
// 거리를 구한 정점들을 반복문으로 돌면서
// 같은 루트를 갖지 않는, 아직 연결되지 않은 정점들을 union 연산하고 값을 더해준다

const unionSet = function(x, y) {
    const px = findSet(x)
    const py = findSet(y)

    p[py] = px
}

const findSet = function(x) {
    if (p[x] === x) {
        return p[x]
    }

    p[x] = findSet(p[x])
    return p[x]
}

const getDistance = function(first, second) {
    const [firstY, firstX] = first
    const [secondY, secondX] = second

    const dist = Math.sqrt(Math.abs(firstY - secondY) ** 2 + Math.abs(firstX - secondX) ** 2, 2)
    return dist
}

const fs = require('fs')
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n')

const [N, M] = input[0].split(' ').map(v => Number(v))
let coordinates = []

for (let i = 1; i <= N; i++) {
    const coordinate = input[i].split(' ').map(v => Number(v))
    coordinates.push(coordinate)
}

let linkedIdx = []

for (let i = N + 1; i < N + 1 + M; i++) {
    const idx = input[i].split(' ').map(v => Number(v))
    linkedIdx.push(idx)
}

let p = new Array(N + 1).fill(0)
for (let i = 1; i <= N; i++) {
    p[i] = i
}

for (let i = 0; i < linkedIdx.length; i++) {
    const [a, b] = linkedIdx[i]

    unionSet(a, b)
}

let distances = []
for (let i = 0; i < coordinates.length - 1; i++) {
    const firstDistance = coordinates[i]

    for (let j = i + 1; j < coordinates.length; j++) {
        const secondDistance = coordinates[j]
        const d = getDistance(firstDistance, secondDistance)

        distances.push([i + 1, j + 1, d])
    }
}

distances.sort((a, b) => {
    return a[2] - b[2]
})

let sums = 0
for (let i = 0; i < distances.length; i++) {
    const [start, end, value] = distances[i]

    if (findSet(start) === findSet(end)) {
        continue
    }

    unionSet(start, end)
    sums += value
}

console.log(sums.toFixed(2))
