const Node = function(value, next = null) {
    this.value = value
    this.next = next
}

const Queue = function() {
    this.head = new Node(null)
    this.tail = this.head
}

Queue.prototype.isEmpty = function() {
    if (this.head.value === null) {
        return true
    }
    return false
}

Queue.prototype.enQueue = function(item) {
    if (this.isEmpty()) {
        this.head = new Node(item)
        this.tail = this.head
    } else {
        let cur = this.tail
        this.tail = new Node(item)
        cur.next = this.tail
    }
}

Queue.prototype.deQueue = function() {
    if (this.isEmpty()) {
        console.log("queue is empty")
        return
    } else {
        const number = this.head.value

        if (this.head === this.tail) {
            this.head = new Node(null)
            this.tail = this.head
        } else {
            const number = this.head.value
            this.head = this.head.next
        }

        return number
    }
}

const findMaxNumberOrZero = function() {
    let maxNumber = 0
    for (let i = 0; i < N; i++) {
        for (let j = 0; j < M; j++) {
            if (tomatoes[i][j] === 0) {
                return -1
            }
            maxNumber = Math.max(maxNumber, tomatoes[i][j])
        }
    }
    return maxNumber - 1
}

const findTomato = function() {
    let q = new Queue()
    for (let i = 0; i < N; i++) {
        for (let j = 0; j < M; j++) {
            if (tomatoes[i][j] === 1) {
                q.enQueue([i, j])
            }
        }
    }
    return q
}

const bfs = function() {
    const queue = findTomato()

    if (queue.length === M * N) {
        return 0
    }

    let yAxis = [-1, 0, 1, 0]
    let xAxis = [0, 1, 0, -1]

    let maxDays = 0
    while (!queue.isEmpty()) {
        const [y, x] = queue.deQueue()
        for (let i = 0; i < 4; i++) {
            const yIdx = y + yAxis[i]
            const xIdx = x + xAxis[i]

            if (0 <= yIdx && yIdx < N && 0 <= xIdx && xIdx < M) {
                if (tomatoes[yIdx][xIdx] === 0) {
                    tomatoes[yIdx][xIdx] = tomatoes[y][x] + 1
                    queue.enQueue([yIdx, xIdx])
                    maxDays = Math.max(maxDays, tomatoes[yIdx][xIdx])
                }
            }
        }
    }
    const result = findMaxNumberOrZero()
    return result
}

const fs = require('fs')
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n')

const [M, N] = input[0].split(' ').map(v => parseInt(v))
let tomatoes = []
for (let i = 1; i <= N; i++) {
    const tomato = input[i].split(' ').map(v => parseInt(v))
    tomatoes.push(tomato)
}

const answer = bfs()
console.log(answer)
