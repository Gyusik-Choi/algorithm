const Node = function(value, next = null) {
    this.value = value
    this.next = next
}

const Queue = function() {
    this.head = new Node(null)
    this.tail = this.head
}

Queue.prototype.isEmpty = function() {
    return this.head.value === null && this.tail.value === null
}

Queue.prototype.enQueue = function(value) {
    if (this.isEmpty()) {
        this.head = new Node(value)
        this.tail = this.head
    } else {
        const tail = this.tail
        this.tail = new Node(value)
        tail.next = this.tail
    }
}

Queue.prototype.deQueue = function() {
    if (this.isEmpty() === false) {
        const popNumber = this.head.value

        if (this.head === this.tail) {
            this.head = new Node(null)
            this.tail = this.head
        } else {
            this.head = this.head.next
        }

        return popNumber
    }

    return popNumber
}

const bfs = function() {
    let q = new Queue()
    q.enQueue([0, 0, 0])
    // 이 코드가 반드시 있어야 한다
    // 시작점을 방문체크 안하게 되면 오답이 나온다
    visited[0][0][0] = 1

    const yAxis = [-1, 0, 1, 0]
    const xAxis = [0, 1, 0, -1]

    // Queue { head: Node { value: null, next: null }, tail: Node { value: null, next: null }}
    // 위와 같은 경우에도 while (q)에 걸리지 않아서 q.deQueue()에서 오류 발생해서 코드 수정
    // while (q) {

    while (q.isEmpty() === false) {
        const [y, x, isBreak] = q.deQueue()

        if (y === N - 1 && x === M - 1) {
            return visited[y][x][isBreak]
        }

        for (let k = 0; k < 4; k++) {
            const yIdx = yAxis[k] + y
            const xIdx = xAxis[k] + x

            if (0 <= yIdx && yIdx < N && 0 <= xIdx && xIdx < M) {
                // 주의할것!
                // console.log(false === 0) 
                // => false
                // if (visited[yIdx][xIdx][isBreak] === false) {
                if (visited[yIdx][xIdx][isBreak] === 0) {
                    if (maps[yIdx][xIdx] === 0) {
                        visited[yIdx][xIdx][isBreak] = visited[y][x][isBreak] + 1
                        q.enQueue([yIdx, xIdx, isBreak])
                    } else {
                        if (isBreak === 0) {
                            visited[yIdx][xIdx][isBreak + 1] = visited[y][x][isBreak] + 1
                            q.enQueue([yIdx, xIdx, isBreak + 1])
                        }
                    }
                }
            }
        }
    }

    return -1
}

const fs = require('fs')
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n')
const [N, M] = input[0].split(' ').map(v => parseInt(v))

let maps = []
for (let i = 1; i <= N; i++) {
    const mapItem = input[i].split('').map(v => parseInt(v))
    maps.push(mapItem)
}

let visited = new Array(N).fill(0).map(v => new Array(M).fill(0).map(v => new Array(2).fill(0)))

// 문제에서는 언급하지 않았지만 다른분들의 코드를 보니 출발점이 1인 경우는 없는듯 하다
// 그리고 도착점도 1인 경우는 없는듯 하다
if (maps[0][0] === 1) {
    console.log(-1)
} else {
    const answer = bfs()
    console.log(answer)
}

// 최단거리 문제라 bfs
// 0은 부순적이 있든 없든 통과 가능
// 1은 부순적이 있으면 통과 못하고 부순적 없으면 통과할 수 있다
// 부순적이 있는지 없는지 체크하는 배열이 필요하다
// visited 배열을 3차원으로 구성
// 부순적 없는 세계와 부순적 있는 세계가 공존
// 부순적이 있는 요소가 1에 오면 통과시키면 안 되고
// 부순적이 없는 요소가 1에 오면 통과시켜야 한다
// 방문 배열에서 한 점을 두 개의 요소로 두는 것은
// 부순적 있는 요소가 통과한 것인지 아니면 부순적 없는 요소가 통과한 것인지 구분하기 위해서
// https://kscodebase.tistory.com/66