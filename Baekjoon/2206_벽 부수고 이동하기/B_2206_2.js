const Node = function(value, next = null) {
    this.value = value
    this.next = next
}

const Queue = function() {
    this.head = new Node(null)
    this.tail = this.head
}

Queue.prototype.isEmpty = function() {
    return this.head.value === null
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
        const popItem = this.head.value

        if (this.head === this.tail) {
            this.head = new Node(null)
            this.tail = this.head
        } else {
            this.head = this.head.next
        }

        return popItem
    }
}

const isValidRange = function(y, x) {
    if (0 <= y && y < N && 0 <= x && x < M) {
        return true
    }

    return false
}

const getVisitedArray = function() {
    return new Array(N).fill(0).map(v => new Array(M).fill(0).map(v => new Array(2).fill(0)))
}

const bfs = function() {
    const q = new Queue()
    q.enQueue([0, 0, 0])

    let visited = getVisitedArray()

    const yDirection = [-1, 0, 1, 0]
    const xDirection = [0, 1, 0, -1]

    while (q.isEmpty() === false) {
        const [y, x, from] = q.deQueue()
        if (y === N - 1 && x === M - 1) {
            return visited[y][x][from] + 1
        }

        for (let j = 0; j < 4; j++) {
            const yIdx = y + yDirection[j]
            const xIdx = x + xDirection[j]

            if (isValidRange(yIdx, xIdx)) {
                // from 의 값을 이 시점에서는 0인지 1인지 알 수 없다
                // 그래서 여기서 if 문으로 검사하면
                // from 값이 0, 1 인 경우 모두 커버할 수 있음
                if (visited[yIdx][xIdx][from] === 0) {
                    // 벽 0
                    if (coordinates[yIdx][xIdx] === 0) {
                        visited[yIdx][xIdx][from] = visited[y][x][from] + 1
                        q.enQueue([yIdx, xIdx, from])
                    // 벽 1
                    } else {
                        // 벽 안 부쉈음
                        if (from === 0) {
                            visited[yIdx][xIdx][from + 1] = visited[y][x][from] + 1
                            q.enQueue([yIdx, xIdx, from + 1])
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

const [N, M] = input[0].split(' ').map(v => Number(v))
let coordinates = []

for (let i = 1; i <= N; i++) {
    const coordinate = input[i].split('').map(v => Number(v))
    coordinates.push(coordinate)
}

const minDistance = bfs()
console.log(minDistance)
