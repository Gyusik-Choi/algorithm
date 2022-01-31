const Node = function(value, next = null) {
    this.value = value
    this.next = next
}

const Queue = function() {
    this.head = new Node(null)
    this.tail = this.head
}

Queue.prototype.isEmpty = function() {
    if (this.head.value === null && this.tail.value === null) {
        return true
    }

    return false
}

Queue.prototype.enQueue = function(item) {
    if (this.isEmpty()) {
        this.head = new Node(item)
        this.tail = this.head
    } else {
        const tail = this.tail
        this.tail = new Node(item)
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
}

const isAllRipen = function() {
    for (let i = 0; i < H; i++) {
        for (let j = 0; j < N; j++) {
            for (let k = 0; k < M; k++) {
                if (boxes[i][j][k] === 0) {
                    return false
                }
            }
        }
    }

    return true
}

const isValidRange = function(h, n, m) {
    if (0 <= h && h < H && 0 <= n && n < N && 0 <= m && m < M) {
        return true
    }

    return false
}

const bfs = function(q) {
    let maxDay = 1

    const zDirection = [-1, 1, 0, 0, 0, 0]
    const yDirection = [0, 0, -1, 0, 1, 0]
    const xDirection = [0, 0, 0, 1, 0, -1]

    while (q.isEmpty() === false) {
        const [z, y, x] = q.deQueue()

        for (let i = 0; i < 6; i++) {
            const zIdx = z + zDirection[i]
            const yIdx = y + yDirection[i]
            const xIdx = x + xDirection[i]

            if (isValidRange(zIdx, yIdx, xIdx)) {
                if (boxes[zIdx][yIdx][xIdx] === 0) {
                    boxes[zIdx][yIdx][xIdx] = boxes[z][y][x] + 1
                    maxDay = Math.max(maxDay, boxes[zIdx][yIdx][xIdx])
                    q.enQueue([zIdx, yIdx, xIdx])
                }
            }
        }
    }

    return maxDay
}

const fs = require('fs')
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n')

const [M, N, H] = input[0].split(' ').map(v => parseInt(v))
let boxes = []

let idx = 1
for (let i = 0; i < H; i++) {
    let box = []
    for (let j = idx; j < idx + N; j++) {
        const oneBox = input[j].split(' ').map(v => parseInt(v))
        box.push(oneBox)
    }
    boxes.push(box)
    idx += N
}

const deq = new Queue()

for (let i = 0; i < H; i++) {
    for (let j = 0; j < N; j++) {
        for (let k = 0; k < M; k++) {
            if (boxes[i][j][k] === 1) {
                deq.enQueue([i, j, k])
                
            }
        }
    }
}

const answer = bfs(deq)

if (isAllRipen()) {
    console.log(answer - 1)
} else {
    console.log(-1)
}
