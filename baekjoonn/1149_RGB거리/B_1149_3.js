const fs = require('fs')
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n')

const N = parseInt(input[0])
let costs = []
for (let i = 1; i <= N; i++) {
    const cost = input[i].split(' ').map(v => Number(v))
    costs.push(cost)
}

let dpRed = new Array(N + 1).fill(0)
let dpGreen = new Array(N + 1).fill(0)
let dpBlue = new Array(N + 1).fill(0)

dpRed[1] = costs[0][0]
dpGreen[1] = costs[0][1]
dpBlue[1] = costs[0][2]

for (let j = 2; j <= N; j++) {
    dpRed[j] = Math.min(dpGreen[j - 1], dpBlue[j - 1]) + costs[j - 1][0]
    dpGreen[j] = Math.min(dpRed[j - 1], dpBlue[j - 1]) + costs[j - 1][1]
    dpBlue[j] = Math.min(dpRed[j - 1], dpGreen[j - 1]) + costs[j - 1][2]
}

console.log(Math.min(dpRed[N], dpGreen[N], dpBlue[N]))
