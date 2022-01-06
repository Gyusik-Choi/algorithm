const unionSet = function(x, y) {
    const px = findSet(x)
    const py = findSet(y)

    p[py] = px
}

const findSet = function(x) {
    if (p[x] === x) return p[x]
    
    p[x] = findSet(p[x])
    return p[x]
}

const fs = require('fs')
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n')

const N = parseInt(input[0])
let xIdx = []
let yIdx = []
let zIdx = []

for (let i = 1; i <= N; i++) {
    const [x, y, z] = input[i].split(' ').map(v => parseInt(v))
    xIdx.push([x, i])
    yIdx.push([y, i])
    zIdx.push([z, i])
}

xIdx.sort((a, b) => a[0] - b[0])
yIdx.sort((a, b) => a[0] - b[0])
zIdx.sort((a, b) => a[0] - b[0])

let distances = []

for (let i = 1; i < N; i++) {
    // 위에서 좌표 값을 기준으로 오름차순 정렬을 이미 했기 때문에 절대값을 구할 필요 없다
    const xDistance = xIdx[i][0] - xIdx[i - 1][0]
    const yDistance = yIdx[i][0] - yIdx[i - 1][0]
    const zDistance = zIdx[i][0] - zIdx[i - 1][0]
    
    distances.push([xDistance, xIdx[i][1], xIdx[i - 1][1]])
    distances.push([yDistance, yIdx[i][1], yIdx[i - 1][1]])
    distances.push([zDistance, zIdx[i][1], zIdx[i - 1][1]])
}

distances.sort((a, b) => a[0] - b[0])

let p = new Array(N + 1).fill(0)
p.forEach((v, i) => {
    p[i] = i
})

let sums = 0

distances.forEach((val, idx) => {
    const [value, start, end] = val

    if (findSet(start) !== findSet(end)) {
            sums += value
            unionSet(start, end)
        }
})
        
console.log(sums)
