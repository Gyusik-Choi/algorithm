const fs = require('fs')
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n')

const T = parseInt(input[0])
let idx = 1
for (let t = 0; t < T; t++) {

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
    }

    const bfs = function() {
        const q = new Queue()
        q.enQueue([startY, startX])
        chessBoard[startY][startX] = 1

        const yAxis = [-2, -1, 1, 2, 2, 1, -1, -2]
        const xAxis = [1, 2, 2, 1, -1, -2, -2, -1]

        while (q.isEmpty() === false) {
            const [y, x] = q.deQueue()
            
            if (y === endY && x === endX) {
                return chessBoard[endY][endX] - 1
            }
            
            for (let i = 0; i < 8; i++) {
                const yWay = y + yAxis[i]
                const xWay = x + xAxis[i]

                if (0 <= yWay && yWay < N && 0 <= xWay && xWay < N) {
                    if (chessBoard[yWay][xWay] === 0) {
                        chessBoard[yWay][xWay] = chessBoard[y][x] + 1
                        q.enQueue([yWay, xWay])
                    }
                }
            }
        }
    }

    const N = parseInt(input[idx])
    const [startY, startX] = input[idx + 1].split(' ').map(v => parseInt(v))
    const [endY, endX] = input[idx + 2].split(' ').map(v => parseInt(v))
    
    let chessBoard = new Array(N).fill(0).map(v => new Array(N).fill(0))
    const answer = bfs()
    idx += 3
    console.log(answer)
}