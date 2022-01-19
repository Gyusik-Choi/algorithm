const dfsRecursion = function(start, visited) {
    if (edges[start].length > 0) {
        for (let j = 0; j < edges[start].length; j++) {
            const vertex = edges[start][j]

            if (dfsRecursionVisited[vertex] === false) {
                dfsRecursionVisited[vertex] = true
                visited.push(vertex)
                dfsRecursion(vertex, visited)
            }
        }
    }

    return visited
}

const bfs = function(start) {
    let queue = [start]
    let visited = []
    let visitedCheck = new Array(N + 1).fill(false)

    while (queue.length > 0) {
        const vertex = queue.shift()
        
        if (visitedCheck[vertex] === false) {
            visited.push(vertex)
            visitedCheck[vertex] = true
            
            if (edges[vertex].length > 0) {
                for (let k = 0; k < edges[vertex].length; k++) {
                    const node = edges[vertex][k]
    
                    // 여기서 queue.includes(node) === false 코드를 추가하지 않고
                    // 위쪽에 if (visitedCheck[vertex] === false) 로 검사했다
                    if (visitedCheck[node] === false) {
                        queue.push(node)
                    }
                }
            }
        }
    }

    return visited
}

const fs = require('fs')
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n')

const [N, M, V] = input[0].split(' ').map(v => Number(v))
let edges = new Array(N + 1).fill(0).map(v => new Array())

for (let i = 1; i <= M; i++) {
    const [s, e] = input[i].split(' ').map(v => Number(v))
    edges[s].push(e)
    edges[e].push(s)
}

edges.forEach((v, i) => {
    v.sort((first, second) => first - second)
})

let dfsRecursionVisited = new Array(N + 1).fill(false)
dfsRecursionVisited[V] = true

const dfsRecursionResult = dfsRecursion(V, [V])
const bfsResult = bfs(V)

console.log(dfsRecursionResult.join(' '))
console.log(bfsResult.join(' '))
