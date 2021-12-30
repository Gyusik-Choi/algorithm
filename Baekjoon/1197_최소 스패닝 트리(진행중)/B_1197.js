const MinHeap = function() {
    this.arr = [null]
}

MinHeap.prototype.heapPush = function(value) {
    this.arr.push(value)
    let idx = this.arr.length - 1
    
    while (idx > 1) {
        if (this.arr[Math.floor(idx / 2)][0] > this.arr[idx][0]) {
            const number = this.arr[Math.floor(idx / 2)]
            this.arr[Math.floor(idx / 2)] = this.arr[idx]
            this.arr[idx] = number

            idx = Math.floor(idx / 2)
        } else {
            break
        }
    }
}

MinHeap.prototype.heapPop = function() {
    if (this.arr.length > 1) {
        const popIdx = this.arr.length - 1

        const number = this.arr[popIdx]
        this.arr[popIdx] = this.arr[1]
        this.arr[1] = number
        this.arr.pop()

        this.minHeapify(1)
        return number
    }

}

MinHeap.prototype.minHeapify = function(idx) {
    let parent = idx
    let leftChild = idx * 2
    let rightChild = idx * 2 + 1

    // 예를들어 [null, 1, 2] 인 상황에서 this.arr.length 는 2가 아니라 3임에 유의
    if (leftChild < this.arr.length && this.arr[parent][0] > this.arr[leftChild][0]) {
        parent = leftChild
    }

    if (rightChild < this.arr.length && this.arr[parent][0] > this.arr[rightChild][0]) {
        parent = rightChild
    }

    if (parent !== idx) {
        const temp = this.arr[parent]
        this.arr[parent] = this.arr[idx]
        this.arr[idx] = temp

        return this.minHeapify(parent)
    }

}

const fs = require('fs')
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n')

const [V, E] = input[0].split(' ').map(v => Number(v))
let edges = new Array(V + 1).fill(0).map(v => new Array())

for (let i = 1; i <= E; i++) {
    const [s, e, v] = input[i].split(' ').map(v => Number(v))
    edges[s].push([e, v])
    edges[e].push([s, v])
}

let mst = new Array(V + 1).fill(false)
let key = new Array(V + 1).fill(Infinity)
key[1] = 0

let minHeap = new MinHeap()
minHeap.heapPush([0, 1])

let answer = 0
while (minHeap.arr.length > 1) {
    const [value, start] = minHeap.heapPop()

    if (!mst[start]) {
        mst[start] = true
        answer += value

        edges[start].forEach((edge) => {
            const [end, val] = edge
            if (!mst[end] && key[end] > val) {
                key[end] = val
                minHeap.heapPush([val, end])
            }
        })
    }
}

console.log(answer)
