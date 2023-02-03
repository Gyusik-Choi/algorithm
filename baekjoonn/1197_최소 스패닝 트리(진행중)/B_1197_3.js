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

const fs = require('fs')
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n')

const [V, E] = input[0].split(' ').map(v => Number(v))
let edges = []

for (let i = 1; i <= E; i++) {
    const [s, e, v] = input[i].split(' ').map(v => Number(v))
    edges.push([s, e, v])
}

edges.sort((first, second) => {
    if (first[2] === second[2]) {
        return first[2] - second[2]
    }
    return first[2] - second[2]
})

let p = [0]
for (let i = 1; i <= V; i++) {
    p.push(i)
}

let cnt = 0
let sums = 0

for (let i = 0; i < E; i++) {
    const [start, end, value] = edges[i]

    if (findSet(start) === findSet(end)) {
        continue
    }

    unionSet(start, end)
    sums += value

    cnt += 1
    if (cnt === V - 1) {
        break
    }
}

console.log(sums)
