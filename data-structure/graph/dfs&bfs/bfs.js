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
                if (visited[e] === false && queue.includes(e) === false) {
                    visited[e] = true
                    queue.push(e)
                }
            })
        }
    }

    return answer
}

const input = ['5 5 3', '5 4', '5 2', '1 2', '3 4', '3 1']

const [N, M, V] = input[0].split(' ').map(v => Number(v))
let edges = new Array(N + 1).fill(0).map(v => new Array())

for (let i = 1; i <= M; i++) {
    const [node1, node2] = input[i].split(' ').map(v => Number(v))
    edges[node1].push(node2)
    edges[node2].push(node1)
}

bfs_visited = bfs(V)
console.log(bfs_visited.join(' '))
