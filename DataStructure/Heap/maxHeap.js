const Heap = function() {
    this.arr = [null];
}

Heap.prototype.heapPush = function(value) {
    this.arr.push(value);
    
    let idx = this.arr.length - 1;
    while (idx > 1) {
        const parentIdx = Math.floor(idx / 2);
        
        if (this.arr[parentIdx] < this.arr[idx]) {
            const temp = this.arr[idx];
            this.arr[idx] = this.arr[parentIdx];
            this.arr[parentIdx] = temp;
            idx = Math.floor(idx / 2);
        } else {
            break;
        }
    }
}

Heap.prototype.heapPop = function() {
    const maxIdx = this.arr.length - 1;

    const temp = this.arr[1];
    this.arr[1] = this.arr[maxIdx];
    this.arr[maxIdx] = temp;

    const popItem = this.arr.pop()
    this.maxHeapify(1);
    console.log(popItem);
    return popItem;
}

Heap.prototype.maxHeapify = function(idx) {
    let parentIdx = idx;
    const leftChildIdx = idx * 2;
    const rightChildIdx = idx * 2 + 1;

    if (leftChildIdx < this.arr.length && this.arr[parentIdx] < this.arr[leftChildIdx]) {
        parentIdx = leftChildIdx;
    }

    if (rightChildIdx < this.arr.length && this.arr[parentIdx] < this.arr[rightChildIdx]) {
        parentIdx = rightChildIdx;
    }

    if (parentIdx !== idx) {
        const temp = this.arr[idx];
        this.arr[idx] = this.arr[parentIdx];
        this.arr[parentIdx] = temp;

        this.maxHeapify(parentIdx);
    }
}

const heap = new Heap();
heap.heapPush(1);
heap.heapPush(2);
heap.heapPush(3);
heap.heapPush(4);
heap.heapPush(5);
heap.heapPush(6);
heap.heapPush(7);
heap.heapPush(8);
heap.heapPush(9);
heap.heapPush(10);
heap.heapPop();
heap.heapPop();
heap.heapPop();
heap.heapPop();
heap.heapPop();
heap.heapPop();
heap.heapPop();
heap.heapPop();
heap.heapPop();
heap.heapPop();
console.log(heap.arr);
