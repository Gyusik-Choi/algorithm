// const fs = require('fs')
// const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n')

const unionSet = function(firstItem, secondItem) {
    const px = findSet(firstItem)
    const py = findSet(secondItem)

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

    const sqrtValue = Math.sqrt(Math.pow(Math.abs(firstY - secondY), 2) + Math.pow(Math.abs(firstX - secondX), 2))
    return sqrtValue
}

const input = [
'3',
'1.0 1.0',
'2.0 2.0',
'2.0 4.0'
]

const n = parseInt(input[0])
let coordinates = []

for (let i = 1; i <= n; i++) {
    const [y, x] = input[i].split(' ').map(v => parseInt(v))
    coordinates.push([y, x])
}

let distances = []

for (let i = 0; i < n - 1; i++) {
    for (let j = i + 1; j < n; j++) {
        const sqrtVal = getDistance(coordinates[i], coordinates[j])
        const distance = [coordinates[i], coordinates[j], sqrtVal]
        distances.push(distance)
    }
}

distances.sort((first, second) => {
    return first[2] - second[2]
})


let p = new Array(distances.length).fill(0)
for (let i = 1; i <= distances.length; i++) {
    p[i] = i
}

let cnt = 0
let sums = 0

for (let i = 0; i < distances.length; i++) {
    const [start, end, value] = distances[i]

    if (findSet(start) === findSet(end)) {
        continue
    }

    unionSet(start, end)
    sums += value

    cnt += 1
    if (cnt === distances.length - 1) {
        break
    }
}

console.log(sums)
