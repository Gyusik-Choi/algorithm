const MinHeap = function() {
    this.arr = [null]

    this.insert = function(item) {
        this.arr.push(item)

        let idx = this.arr.length - 1
        while (idx > 1) {
            if (this.arr[Math.floor(idx / 2)] > this.arr[idx]) {
                let temp = this.arr[idx]
                this.arr[idx] = this.arr[Math.floor(idx / 2)]
                this.arr[Math.floor(idx / 2)] = temp

                idx = Math.floor(idx / 2)
            } else {
                break
            }
        }
    }

    this.remove = function() {
        if (this.arr.length < 2) {
            return
        }

        if (this.arr.length < 3) {
            const item = this.arr.pop()
            return item
        }
        
        let temp = this.arr[this.arr.length - 1]
        this.arr[this.arr.length - 1] = this.arr[1]
        this.arr[1] = temp

        const item = this.arr.pop()
        this.minHeapify(1)
        return item
    }

    this.minHeapify = function(idx) {
        let parentIdx = idx
        let leftChildIdx = idx * 2
        let rightChildIdx = idx * 2 + 1

        if (parentIdx * 2 < this.arr.length && this.arr[parentIdx] > this.arr[leftChildIdx]) {
            parentIdx = leftChildIdx
        } 

        if (parentIdx * 2 + 1 < this.arr.length && this.arr[parentIdx] > this.arr[rightChildIdx]) {
            parentIdx = rightChildIdx
        }

        if (parentIdx != idx) {
            let temp = this.arr[parentIdx]
            this.arr[parentIdx] = this.arr[idx]
            this.arr[idx] = temp

            this.minHeapify(parentIdx)
        }
    }
}

let minHeap = new MinHeap()
minHeap.insert(10)
minHeap.insert(9)
minHeap.insert(8)
minHeap.insert(7)
minHeap.insert(6)
minHeap.insert(5)
minHeap.insert(4)
minHeap.insert(3)
minHeap.insert(2)
minHeap.insert(1)
console.log(minHeap)
minHeap.remove()
minHeap.remove()
minHeap.remove()
minHeap.remove()
minHeap.remove()
minHeap.remove()
minHeap.remove()
minHeap.remove()
minHeap.remove()
console.log(minHeap)