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

const input = ['5 5 3', '5 4', '5 2', '1 2', '3 4', '3 1']

const [N, M, V] = input[0].split(' ').map(v => Number(v))
let edges = new Array(N + 1).fill(0).map(v => new Array())

for (let i = 1; i <= M; i++) {
    const [node1, node2] = input[i].split(' ').map(v => Number(v))
    edges[node1].push(node2)
    edges[node2].push(node1)
}

dfs_visited = dfsRecursion(V, [V])