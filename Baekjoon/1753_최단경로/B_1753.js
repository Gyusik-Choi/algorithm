const fs = require('fs')
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n')

const VE = input[0].split(' ').map(v => parseInt(v))
const V = VE[0]
const E = VE[1]

const K = parseInt(input[1])

let routes = new Array(V + 1).fill(0).map(v => new Array())
for (let i = 2; i < E + 2; i++) {
    const route = input[i].split(' ').map(v => parseInt(v))
    const idx = route[0]
    routes[idx].push(route)
}

let distance = new Array(V + 1).fill(Infinity)
distance[K] = 0

let selected = new Array(V + 1).fill(false)

let cnt = 0

while (cnt < V - 1) {
    let smallestValue = Infinity
    let smallestIdx = -1

    for (let i = 1; i <= V; i++) {
        if (selected[i] === false && distance[i] < smallestValue) {
            smallestValue = distance[i]
            smallestIdx = i
        }
    }
    
    selected[smallestIdx] = true

    if (smallestIdx != -1 && routes[smallestIdx].length > 0) {
        routes[smallestIdx].forEach((item, index) => {
            const e = item[1]
            const v = item[2]

            if (selected[e] === false && distance[e] > distance[smallestIdx] + v) {
                distance[e] = distance[smallestIdx] + v
            }
        })
    }

    cnt += 1
}

for (let i = 1; i <= V; i++) {
    if (distance[i] === Infinity) {
        console.log("INF")
    } else {
        console.log(distance[i])
    }
}
