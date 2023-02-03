const floydWarshall = function() {
    for (let k = 1; k <= V; k++) {
        for (let i = 1; i <= V; i++) {
            for (let j = 1; j <= V; j++) {
                if (roads[i][j] > roads[i][k] + roads[k][j]) {
                    roads[i][j] = roads[i][k] + roads[k][j]
                }
            }
        }
    }
}

const fs = require('fs')
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n')

const [V, E] = input[0].split(' ').map(v => Number(v))
let roads = new Array(V + 1).fill(Infinity).map(v => new Array(V + 1).fill(Infinity))

for (let i = 1; i <= E; i++) {
    const [a, b, c] = input[i].split(' ').map(v => Number(v))
    roads[a][b] = c
}

floydWarshall()

let smallestDistance = Infinity
for (let i = 1; i <= V - 1; i++) {
    for (let j = i + 1; j <= V; j++) {
        if (smallestDistance > roads[i][j] + roads[j][i]) {
            smallestDistance = roads[i][j] + roads[j][i]
        }
    }
}

console.log(smallestDistance === Infinity ? -1 : smallestDistance)

// 참고
// https://blog.naver.com/ndb796/221234427842
// https://imnotabear.tistory.com/197
