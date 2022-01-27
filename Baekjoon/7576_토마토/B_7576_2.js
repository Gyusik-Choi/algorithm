const Node = function(value, next = null) {
    this.value = value
    this.next = next
}

const Deque = function() {
    this.head = new Node(null)
    this.tail = this.head
}

Deque.prototype.isEmpty = function() {
    if (this.head.value === null) {
        return true
    }
    return false
}

Deque.prototype.enQueue = function(item) {
    if (this.isEmpty()) {
        this.head = new Node(item)
        this.tail = this.head
    } else {
        const tail = this.tail
        this.tail = new Node(item)
        tail.next = this.tail
    }
}

Deque.prototype.deQueue = function() {
    if (!this.isEmpty()) {
        const val = this.head.value

        if (this.head === this.tail) {
            this.head = new Node(null)
            this.tail = this.head
        } else {
            this.head = this.head.next
        }

        return val
    }
}

const isAllRipen = function(visited) {
    for (let i = 0; i < N; i++) {
        for (let j = 0; j < M; j++) {
            if (visited[i][j] === 0) {
                return false
            }
        }
    }

    return true
}

const bfs = function(q, visited) {
    // 최소 날짜지만 완료된 날짜인만큼 최대 날짜가 될 것이다
    let finishDay = 0
    
    const yDirection = [-1, 0, 1, 0]
    const xDirection = [0, 1, 0, -1]

    while (!q.isEmpty()) {
        const [y, x] = q.deQueue()
        for (let i = 0; i < 4; i++) {
            const yIdx = yDirection[i] + y
            const xIdx = xDirection[i] + x

            if (0 <= yIdx && yIdx < N && 0 <= xIdx && xIdx < M) {
                if (visited[yIdx][xIdx] === 0 && boxes[yIdx][xIdx] === 0) {
                    visited[yIdx][xIdx] = visited[y][x] + 1
                    finishDay = Math.max(finishDay, visited[yIdx][xIdx])
                    q.enQueue([yIdx, xIdx])
                }
            }
        }
    }

    if (isAllRipen(visited)) {
        // 0일 경우 -1이 되지 않고 0이 될 수 있도록 처리
        return finishDay === 0 ? finishDay : finishDay - 1
    }

    return -1
}

const findTomato = function(boxes) {
    const deq = new Deque()

    for (let i = 0; i < N; i++) {
        for (let j = 0; j < M; j++) {
            if (boxes[i][j] === 1) {
                deq.enQueue([i, j])
                visited[i][j] = 1
            } else if (boxes[i][j] === -1) {
                visited[i][j] = -1
            }
        }
    }

    return deq
}

const fs = require('fs')
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n')

const [M, N] = input[0].split(' ').map(v => Number(v))
let boxes = []

for (let i = 1; i <= N; i++) {
    const box = input[i].split(' ').map(v => Number(v))
    boxes.push(box)
}

let visited = new Array(N).fill(0).map(v => new Array(M).fill(0))
const queue = findTomato(boxes)

const answer = bfs(queue, visited)
console.log(answer)
