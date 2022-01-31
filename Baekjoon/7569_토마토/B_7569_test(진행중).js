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
        const popNumber = this.tail.value

        if (this.head === this.tail) {
            this.head = new Node(null)
            this.tail = this.head
        } else {
            this.head = this.head.next
        }

        return popNumber
    }
}

const isAllRipen = function(h, n, m) {
    for (let i = 0; i < h; i++) {
        for (let j = 0; j < n; j++) {
            for (let k = 0; k < m; k++) {
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
    // visited 에 날짜를 계산해나갈까 고민했지만
    // visited 는 방문 여부만 체크하고
    // deq 에 담을때 날짜를 계산해서 담아가는 방식으로 진행한다
    // => visited 가 필요없다

    let maxDay = 0

    // let visited = new Array(H).fill(false).map(v => 
    //     new Array(N).fill(false).map(v => 
    //         new Array(M).fill(false)
    //     )
    // )

    const zDirection = [-1, 1, 0, 0, 0, 0]
    const yDirection = [0, 0, -1, 0, 1, 0]
    const xDirection = [0, 0, 0, 1, 0, -1]

    while (q.isEmpty() === false) {
        const [z, y, x] = q.deQueue()
        // visited[z][y][x] = true

        for (let i = 0; i < 6; i++) {
            const zIdx = z + zDirection[i]
            const yIdx = y + yDirection[i]
            const xIdx = x + xDirection[i]

            if (0 <= zIdx && zIdx < H && 0 <= yIdx && yIdx < N && 0 <= xIdx && xIdx < M) {
            // if (isValidRange(zIdx, yIdx, xIdx)) {
                if (boxes[zIdx][yIdx][xIdx] === 0) {
                    // if (visited[zIdx][yIdx][xIdx] === false) {
                    //     boxes[zIdx][yIdx][xIdx] = 1
                    //     maxDay = Math.max(maxDay, day + 1)
                    //     q.enQueue([zIdx, yIdx, xIdx, day + 1])
                    // }
                    boxes[zIdx][yIdx][xIdx] = boxes[z][y][x] + 1
                    maxDay = Math.max(maxDay, boxes[zIdx][yIdx][xIdx])
                    q.enQueue([zIdx, yIdx, xIdx])
                    
                }
            }
        }
    }

    return maxDay
}

const input = [
'5 3 2',
'0 0 0 0 0',
'0 0 0 0 0',
'0 0 0 0 0',
'0 0 0 0 0',
'0 0 1 0 0',
'0 0 0 0 0'
]

// const input = [
// '4 3 2',
// '1 1 1 1',
// '1 1 1 1',
// '1 1 1 1',
// '1 1 1 1',
// '-1 -1 -1 -1',
// '1 1 1 -1'
// ]

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
    console.log(answer === 0 ? 0 : answer - 1)
} else {
    console.log(-1)
}