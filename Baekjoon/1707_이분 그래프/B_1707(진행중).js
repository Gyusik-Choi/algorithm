const fs = require('fs')
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n')

const K = Number(input[0])
let idx = 1
for (let i = 0; i < K; i++) {

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
        if (this.isEmpty() === true) {
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
        q.enQueue(1)
        bipartiteGraph[1] = 1

        while (q.isEmpty() === false) {
            const start = q.deQueue()
            
            if (edges[start].length > 0) {
                // edges[start].forEach((vertex) => {
                const go = edges[start]
                const edgesLength = edges[start].length
                for (let k = 0; k < edgesLength; k++) {
                    const vertex = go[k]
                    if (bipartiteGraph[start] === bipartiteGraph[vertex]) {
                        return false
                    } else {
                        if (bipartiteGraph[vertex] === 0) {
                            if (bipartiteGraph[start] === 1) {
                                bipartiteGraph[vertex] = 2
                            } else {
                                bipartiteGraph[vertex] = 1
                            }
                            q.enQueue(vertex)
                        }
                    }
                }
            } else {
                continue
            }
        }

        return true
    }

    const [V, E] = input[idx].split(' ').map(v => Number(v))
    let edges = new Array(V + 1).fill(0).map(v => new Array())

    for (let j = idx + 1; j <= idx + E; j++) {
        const [vertex1, vertex2] = input[j].split(' ').map(v => Number(v))
        edges[vertex1].push(vertex2)
        edges[vertex2].push(vertex1)
    }

    let bipartiteGraph = new Array(V + 1).fill(0)
    let flag = true

    for (let m = 1; m <= V; m++) {
        if (bipartiteGraph[m] === 0) {
            answer = bfs(m)
            if (answer === false) {
                flag = false
                break
            }
        }
    }

    console.log(flag === true ? "YES" : "NO")
    idx += E + 1
}