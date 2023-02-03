const dfs = function(start) {
    let answer = []
    let visited = new Array(computers + 1).fill(false)
    let stack = []
    stack.push(start)

    while (stack.length > 0) {
        c = stack.pop()
        visited[c] = true
        answer.push(c)

        if (pairs[c].length > 0) {
            pairs[c].forEach((p) => {
                if (visited[p] === false && stack.indexOf(p) === -1) {
                    stack.push(p)
                }
            })
        }
    }

    return answer
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

const answer = dfs(1)
console.log(answer.length - 1)
