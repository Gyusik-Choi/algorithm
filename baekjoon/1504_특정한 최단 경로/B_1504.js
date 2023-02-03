const dijkstra = function(start) {
    let distance = new Array(N + 1).fill(Infinity)
    let selected = new Array(N + 1).fill(false)

    distance[start] = 0
    
    let cnt = 0
    while (cnt < N - 1) {
        // distance에서 최소값 찾기
        let minVal = Infinity
        let minIdx = -1
        for (let i = 1; i <= N; i++) {
            if (!selected[i] && minVal > distance[i]) {
                minVal = distance[i]
                minIdx = i
            }
        }

        // minIdx가 -1이면 갱신되지 않은 것
        // 갈 수 없는 정점들만 있는 상태
        if (minIdx != -1) {
            selected[minIdx] = true
            
            // minIdx를 기준으로 갈 수 있는 정점들에 대한 최소 거리 갱신
            if (nodes[minIdx].length > 0) {
                for (let j = 0; j < nodes[minIdx].length; j++) {
                    const edge = nodes[minIdx][j]

                    const end = edge[1]
                    const value = edge[2]

                    if (!selected[end] && distance[end] > distance[minIdx] + value) {
                        distance[end] = distance[minIdx] + value
                    }
                }
            }
        }

        cnt += 1
    }

    return distance
}

const fs = require('fs')
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n')

const NE = input[0].split(' ').map(v => Number(v))
const N = NE[0]
const E = NE[1]

let nodes = new Array(N + 1).fill(0).map(v => new Array())

// 방향성이 없는 그래프
for (let i = 1; i <= E; i++) {
    const node = input[i].split(' ').map(v => Number(v))

    const s = node[0]
    const e = node[1]
    const v = node[2]

    nodes[s].push([s, e, v])
    nodes[e].push([e, s, v])
}

const v12 = input[input.length - 1].split(' ').map(v => Number(v))
const v1 = v12[0]
const v2 = v12[1]

distanceFrom1 = dijkstra(1)
distanceFromV1 = dijkstra(v1)
distanceFromV2 = dijkstra(v2)

const candidate1 = distanceFrom1[v1] + distanceFromV1[v2] + distanceFromV2[N]
const candidate2 = distanceFrom1[v2] + distanceFromV2[v1] + distanceFromV1[N]

console.log(Math.min(candidate1, candidate2) === Infinity ? -1 : Math.min(candidate1, candidate2))

// 다익스트라
// 1 -> v1 -> v2 -> N
// 1 -> v2 -> v1 -> N
// 1에서 v1 or v2
// v1 -> v2 or v2 -> v1

// 1에서 다익스트라 => 1에서 v1, v2로의 거리 나온다
// v1에서 다익스트라 => v1에서 v2, v1에서 N으로의 거리 나온다
// v2에서 다익스트라 => v2에서 v1, v2에서 N으로의 거리 나온다

// 1 ~ v1 + v1 ~ v2 + v2 ~ N
// 1 ~ v2 + v2 ~ v1 + v1 ~ N
// 둘 중에 최소값

// 다익스트라 3번 필요