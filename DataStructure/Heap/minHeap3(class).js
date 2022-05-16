class MinHeap {
    constructor() {
        this.arr = [null];
    }

    change(parent, child) {
        const parentItem = this.arr[parent];
        const childItem = this.arr[child];

        this.arr[parent] = childItem;
        this.arr[child] = parentItem;
    }

    heapPush(number) {
        this.arr.push(number);
        
        let idx = this.arr.length - 1;
        while (idx > 1) {
            const parentIdx = Math.floor(idx / 2);

            if (this.arr[parentIdx] > this.arr[idx]) {
                this.change(parentIdx, idx);

                idx = Math.floor(idx / 2);
            } else {
                break;
            }
        }
    }

    heapPop() {
        if (this.arr.length > 1) {
            this.change(1, this.arr.length - 1);
            const popItem = this.arr.pop();
            console.log(popItem);
            this.heapify(1);
            return popItem;   
        }
    }

    heapify(idx) {
        let parentIdx = idx;
        const leftChildIdx = idx * 2;
        const rightChildIdx = idx * 2 + 1;

        if (leftChildIdx < this.arr.length) {
            if (this.arr[parentIdx] > this.arr[leftChildIdx]) {
                parentIdx = leftChildIdx;
            }
        }

        if (rightChildIdx < this.arr.length) {
            if (this.arr[parentIdx] > this.arr[rightChildIdx]) {
                parentIdx = rightChildIdx;
            }
        }

        if (idx != parentIdx) {
            this.change(idx, parentIdx);
            return this.heapify(parentIdx);
        }
    }
}

const minHeap = new MinHeap();
minHeap.heapPush(10)
minHeap.heapPush(9)
minHeap.heapPush(8)
minHeap.heapPush(7)
minHeap.heapPush(6)
minHeap.heapPush(5)
minHeap.heapPush(4)
minHeap.heapPush(3)
minHeap.heapPush(2)
minHeap.heapPush(1)
console.log(minHeap)
minHeap.heapPop()
minHeap.heapPop()
minHeap.heapPop()
minHeap.heapPop()
minHeap.heapPop()
minHeap.heapPop()
minHeap.heapPop()
minHeap.heapPop()
minHeap.heapPop()
minHeap.heapPop()
console.log(minHeap)
