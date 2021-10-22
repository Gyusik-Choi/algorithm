const dfsRecursion = function(start, visited) {
    if (pairs[start].length > 0) {
        pairs[start].forEach((p) => {
            if (visited.indexOf(p) === -1) {
                visited.push(p)
                dfsRecursion(p, visited)
            }
        })
    }

    return visited
}

const fs = require('fs')
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n')

const computers = parseInt(input[0])
const computerPairs = parseInt(input[1])

let pairs = new Array(computers + 1).fill(0).map(v => new Array())
for (let i = 2; i < computerPairs + 2; i++) {
    const [s, e] = input[i].split(' ').map(v => Number(v))
    pairs[s].push(e)
    pairs[e].push(s)
}

const visited = dfsRecursion(1, [1])
console.log(visited.length - 1)
