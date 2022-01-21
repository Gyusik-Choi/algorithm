const dfsRecursion = function(start, visited, virusNumber) {
    if (edges[start].length > 0) {
        for (let j = 0; j < edges[start].length; j++) {
            const node = edges[start][j]

            if (visited[node] === false) {
                visited[node] = true
                virusNumber += 1
                // https://www.acmicpc.net/board/view/77055
                // virusNumber는 원시값이라서 하위 재귀에서 넘어온 값을 따로 변수에 담아주지 않으면 
                // 하위 재귀에서의 virusNumber 값을 알 수 없음
                virusNumber = dfsRecursion(node, visited, virusNumber)
            }
        }
    }

    return virusNumber
}

const fs = require('fs')
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n')

const computersNum = parseInt(input[0])
const pairsNum = parseInt(input[1])
let edges = new Array(computersNum + 1).fill(0).map(v => new Array())

for (let i = 2; i < 2 + pairsNum; i++) {
    const [s, e] = input[i].split(' ').map(v => parseInt(v))
    edges[s].push(e)
    edges[e].push(s)
}

let visit = new Array(computersNum + 1).fill(false)
visit[1] = true

const virus = dfsRecursion(1, visit, 0)
console.log(virus)
