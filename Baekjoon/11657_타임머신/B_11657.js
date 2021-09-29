const bellmanFord = function() {
    for (let i = 0; i < M - 1; i++) {
        for (let j = 0; j < M; j++) {
            const start = routes[j][0]
            const end = routes[j][1]
            const value = routes[j][2]

            if (distance[start] != Infinity && distance[end] > distance[start] + value) {
                distance[end] = distance[start] + value
            }
        }
    }

    for (let i = 0; i < 1; i++) {
        for (let j = 0; j < M; j++) {
            const start = routes[j][0]
            const end = routes[j][1]
            const value = routes[j][2]

            if (distance[start] != Infinity && distance[end] > distance[start] + value) {
                return false
            }
        }
    }

    return true
}

const fs = require('fs')
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n')

const NM = input[0].split(' ').map(v => parseInt(v))
const N = NM[0]
const M = NM[1]

let routes = []
for (let i = 1; i <= M; i++) {
    const route = input[i].split(' ').map(v => parseInt(v))
    const s = route[0]
    routes.push(route)
}

let distance = new Array(N + 1).fill(Infinity)
distance[1] = 0

const val = bellmanFord()
if (val) {
    for (let i = 2; i <= N; i++) {
        if (distance[i] != Infinity) {
            console.log(distance[i])
        } else {
            console.log(-1)
        }
    }
} else {
    console.log(-1)
}
