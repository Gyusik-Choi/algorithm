// const dfs = function(start) {
//     let answer = []
//     let visited = new Array(N + 1).fill(false)
//     let stack = [start]
//     visited[start] = true

//     while (stack.length > 0) {
//         const edge = stack.pop()
//         answer.push(edge)
//         if (edges[edge].length > 0) {
//             edges[edge].forEach((e) => {
//                 if (visited[e] === false && stack.includes(e) === false) {
//                     visited[e] = true
//                     stack.push(e)
//                 }
//             })
//         }
//     }
//     return answer
// }
// 문제에서 요구하는 정답대로 탐색을 하기에는 stack방식은 이 문제에서는 활용하기 까다롭다
// 예제 입력1의 경우 stack에 1의 정점은 [2, 3, 4]를 인접 정점으로 받게 된다
// 이러면 스택에는 2, 3, 4가 들어가므로 4부터 나와서 탐색하게 돼서 정답이 1 4 3 2가 나온다

const dfsRecursion = function(start, visited) {
    if (edges[start].length > 0) {
        edges[start].forEach((edge) => {
            if (visited.includes(edge) === false) {
                visited.push(edge)
                dfsRecursion(edge, visited)
            }
        })
    }
    return visited
}

const bfs = function(start) {
    // 방문한 순서를 담는 정답 배열과 방문 여부를 체크하는 배열을 따로 두었다
    let answer = []
    let visited = new Array(N + 1).fill(false)
    let queue = [start]
    visited[start] = true

    while (queue.length > 0) {
        const edge = queue.shift()
        answer.push(edge)
        if (edges[edge].length > 0) {
            edges[edge].forEach((e) => {
                // if (visited[e] === false && queue.includes(e) === false) {
                // indexOf 제출했을때 이 속도가 더 빠르게 나왔다
                if (visited[e] === false && queue.indexOf(e) === -1) {
                    visited[e] = true
                    queue.push(e)
                }
            })
        }
    }

    return answer
}

const fs = require('fs')
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n')

const [N, M, V] = input[0].split(' ').map(v => Number(v))
let edges = new Array(N + 1).fill(0).map(v => new Array())

for (let i = 1; i <= M; i++) {
    const [node1, node2] = input[i].split(' ').map(v => Number(v))
    edges[node1].push(node2)
    edges[node2].push(node1)
}

// 탐색 순서를 정답에서 요구하는데로 맞추기 위해 각 정점들에 대한 인접 정점들을 정렬한다
for (let i = 1; i <= N; i++) {
    edges[i].sort((a, b) => a - b)
}

dfs_visited = dfsRecursion(V, [V])
bfs_visited = bfs(V)

console.log(dfs_visited.join(' '))
console.log(bfs_visited.join(' '))