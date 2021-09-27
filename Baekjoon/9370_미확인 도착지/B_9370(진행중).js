const dijkstra = function(departure, ways) {
    let distance = new Array(n + 1).fill(Infinity)
    let selected = new Array(n + 1).fill(false)

    distance[departure] = 0

    let cnt = 0
    while (cnt < n - 1) {

        let minVal = Infinity
        let minIdx = -1

        for (let idx = 1; idx <= n; idx++) {
            if (!selected[idx] && minVal > distance[idx]) {
                minVal = distance[idx]
                minIdx = idx
            }
        }

        selected[minIdx] = true

        if (minIdx != -1) {
            if (ways[minIdx].length > 0) {
                ways[minIdx].forEach((item) => {
                    const go = item[0]
                    const end = item[1]
                    const val = item[2]
                    
                    if (!selected[end] && distance[end] > distance[minIdx] + val) {
                        distance[end] = distance[minIdx] + val
                    }
                })
            }
        }

        cnt += 1
    }

    return distance
}

const fs = require('fs')
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n')

const T = parseInt(input[0])

// 다익스트라
// s -> 교차로1 -> 교차로2 -> 목적지
// s -> 교차로2 -> 교차로1 -> 목적지

// s 기준 다익스트라를 통해 구한 목적지까지의 거리와 같거나 더 가까워야 가능한 후보로 인정

// 총 다익스트라 3회
// => s로 다익스트라 한번돌기
// => 교차로1에서 목적지
// => 교차로2에서 목적지

// 입력부터 쉽지 않다...
// 파이썬이라면 훨씬 편하게 입력 받았을텐데...
// 입력만 70줄이 넘는다
for (let i = 0; i < T; i++) {
    let start = null

    let nmt = null
    let n = null
    let m = null
    let t = null

    let sgh = null
    let s = null
    let g = null
    let h = null

    // 테스트케이스 첫번째
    if (i === 0) {
        // n 교차로 개수/ m 도로 개수/ t 목적지 후보 개수
        nmt = input[1].split(' ').map(v => parseInt(v))
        n = nmt[0]
        m = nmt[1]
        t = nmt[2]

        // s 예술가 출발지/ g h 예술가가 있는 사이 지점
        sgh = input[2].split(' ').map(v => parseInt(v))
        s = sgh[0]
        g = sgh[1]
        h = sgh[2]

        // 양방향
        let routes = new Array(n + 1).fill(0).map(v => new Array())
        for (let j = 3; j < 3 + m; j++) {
            const route = input[j].split(' ').map(v => parseInt(v))
            const s = route[0]
            const e = route[1]
            const v = route[2]

            routes[s].push([s, e, v])
            routes[e].push([e, s, v])
        }

        let candidates = []
        for (let k = 3 + m; k < 3 + m + t; k++) {
            const candidate = parseInt(input[k])
            candidates.push(candidate)
        }

        const ds = dijkstra(s, routes)
        const dg = dijkstra(g, routes)
        const dh = dijkstra(h, routes)

        let answer = []
        candidates.forEach((candidate) => {
            const first = ds[g] + dg[h] + dh[candidate]
            const second = ds[h] + dh[g] + dg[candidate]

            const smallerDistanceValue = Math.min(first, second)
            if (smallerDistanceValue != Infinity && smallerDistanceValue < ds[candidate]) {
                answer.push(smallerDistanceValue)
            }
        })

        start += 3 + m + t
    // 테스트케이스 두번째부터
    } else {
        nmt = input[start].split(' ').map(v => parseInt(v))
        n = nmt[0]
        m = nmt[1]
        t = nmt[2]

        sgh = input[start + 1].split(' ').map(v => parseInt(v))
        s = sgh[0]
        g = sgh[1]
        h = sgh[2]

        let routes = new Array(n + 1).fill(0).map(v => new Array())
        for (let j = start + 2; j < start + 2 + m; j++) {
            const route = input[j].split(' ').map(v => parseInt(v))
            const s = route[0]
            const e = route[1]
            const v = route[2]

            routes[s].push([s, e, v])
            routes[e].push([e, s, v])
        }

        let candidates = []
        for (let k = start + 2 + m; k < start + 2 + m + t; k++) {
            const candidate = parseInt(input[k])
            candidates.push(candidate)
        }

        const ds = dijkstra(s, routes)
        const dg = dijkstra(g, routes)
        const dh = dijkstra(h, routes)

        start += 2 + k + m
    }

}
