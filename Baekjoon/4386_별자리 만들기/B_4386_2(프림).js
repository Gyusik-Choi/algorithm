const MinHeap = function() {
    this.arr = [null]
}

MinHeap.prototype.heapPush = function(item) {
    this.arr.push(item)

    let idx = this.arr.length - 1
    while (idx > 1) {
        if (this.arr[Math.floor(idx / 2)][0] > this.arr[idx][0]) {
            const toChange = this.arr[Math.floor(idx / 2)]
            this.arr[Math.floor(idx / 2)] = this.arr[idx]
            this.arr[idx] = toChange
            idx = Math.floor(idx / 2)
        } else {
            break
        }
    }
}

MinHeap.prototype.heapPop = function() {
    if (this.arr.length > 1) {
        const item = this.arr[1]
        this.arr[1] = this.arr[this.arr.length - 1]
        this.arr[this.arr.length - 1] = item
        
        const popItem = this.arr.pop()
        this.minHeapify(1)

        return popItem
    }

    return false
}

MinHeap.prototype.minHeapify = function(idx) {
    let parent = idx
    const leftChild = parent * 2
    const rightChild = parent * 2 + 1

    if (leftChild < this.arr.length && this.arr[parent][0] > this.arr[leftChild][0]) {
        parent = leftChild
    }

    if (rightChild < this.arr.length && this.arr[parent][0] > this.arr[rightChild][0]) {
        parent = rightChild
    }

    if (parent !== idx) {
        const originParent = this.arr[idx]
        this.arr[idx] = this.arr[parent]
        this.arr[parent] = originParent
        return this.minHeapify(parent)
    }
}

const getDistance = function(first, second) {
    const [firstY, firstX] = first
    const [secondY, secondX] = second
    
    return Math.sqrt(Math.pow(Math.abs(firstY - secondY), 2) + Math.pow(Math.abs(firstX - secondX), 2))
}

const fs = require('fs')
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n')

const n = parseInt(input[0])
let coordinates = []

for (let i = 1; i <= n; i++) {
    const coordinate = input[i].split(' ').map(v => parseInt(v))
    coordinates.push(coordinate)
}

let distances = new Array(n).fill(0).map(v => new Array())
for (let i = 0; i < n; i++) {
    const firstItem = coordinates[i]
    for (let j = 0; j < n; j++) {
        if (i === j) {
            continue
        }

        const secondItem = coordinates[j]
        const distance = getDistance(firstItem, secondItem)

        distances[i].push([distance, j])
        // distances[j].push([distance, i])
    }
}

let mst = new Array(distances.length).fill(false)
let p = new Array(distances.length).fill(Infinity)

p[0] = 0

const minHeap = new MinHeap()
minHeap.heapPush([0, 0])

let answer = 0
while (minHeap.arr.length > 1) {
    const [value, start] = minHeap.heapPop()

    if (mst[start] === false) {
        mst[start] = true
        answer += value

        if (distances[start].length > 0) {
            distances[start].forEach((v, i) => {
                const [val, go] = v

                if (mst[go] === false && p[go] > val) {
                    p[go] = val
                    minHeap.heapPush([val, go])
                }
            })
        }
    }
}

console.log(answer)
