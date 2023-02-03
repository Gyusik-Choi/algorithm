const floydWarshall = function() {
    for (let i = 1; i <= n; i++) {
        for (let j = 1; j <= n; j++) {
            for (let k = 1; k <= n; k++) {
                if (distance[j][k] > distance[j][i] + distance[i][k]) {
                    distance[j][k] = distance[j][i] + distance[i][k]
                }
            }
        }
    }
}

const fs = require('fs')
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n')

const n = Number(input[0])
const m = Number(input[1])
let distance = new Array(n + 1).fill(Infinity).map(v => new Array(n + 1).fill(Infinity))
for (let i = 1; i <= n; i++) {
    distance[i][i] = 0
}

for (let i = 2; i < input.length; i++) {
    const route = input[i].split(' ').map(v => Number(v))
    
    const a = route[0]
    const b = route[1]
    const c = route[2]
    
    if (distance[a][b] > c) {
        distance[a][b] = c
    }
}

floydWarshall()
for (let i = 1; i <= n; i++) {
    let answer = ''
    for (let j = 1; j <= n; j++) {
        if (distance[i][j] === Infinity) {
            answer += "0 "
        } else {
            answer += distance[i][j] + " "
        }
    }
    console.log(answer)
}