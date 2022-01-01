// 이 heap 구조는 heap에 배열로 값이 입력되는 상황에 맞춰서 구성이 되었다
// 배열의 원소가 2개일 때 첫번째 값을 기준으로만 정렬했던 부분을 수정해서
// 첫번째 값이 같은 경우에는 두번째 값을 기준으로 정렬하도록 했다

// 구현하고 아쉬운 점은 배열이 아니라 그냥 정수를 입력할 경우에는 제대로 동작하지 않으며
// 원소가 2개인 배열이 입력되었을 때만 동작하는 형태라
// 좀 더 다양한 형태의 입력을 커버할 수 있는 형태로 개선하고 싶다

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
        } else if (this.arr[Math.floor(idx / 2)][0] === this.arr[idx][0]) {
            if (this.arr[Math.floor(idx / 2)][1] > this.arr[idx][1]) {
                const number = this.arr[Math.floor(idx / 2)]
                this.arr[Math.floor(idx / 2)] = this.arr[idx]
                this.arr[idx] = number
    
                idx = Math.floor(idx / 2)
            }
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
        
        const popNumber = this.arr.pop()
        this.minHeapify(1)
        return popNumber
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

    if (leftChild < this.arr.length && this.arr[parent][0] === this.arr[leftChild][0]) {
        if (this.arr[parent][1] > this.arr[leftChild][1]) {
            parent = leftChild
        }
    }

    if (rightChild < this.arr.length && this.arr[parent][0] > this.arr[rightChild][0]) {
        parent = rightChild
    }

    if (rightChild < this.arr.length && this.arr[parent][0] === this.arr[rightChild][0]) {
        if (this.arr[parent][1] > this.arr[rightChild][1]) {
            parent = rightChild
        }
    }

    if (parent !== idx) {
        const temp = this.arr[parent]
        this.arr[parent] = this.arr[idx]
        this.arr[idx] = temp

        return this.minHeapify(parent)
    }

}

const minHeap = new MinHeap()
minHeap.heapPush([1, 5])
minHeap.heapPush([1, 4])
minHeap.heapPush([1, 3])
minHeap.heapPush([1, 2])
minHeap.heapPush([1, 1])
console.log(minHeap)
console.log(minHeap.heapPop())
