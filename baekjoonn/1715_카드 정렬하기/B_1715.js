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

const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

const N = parseInt(input[0]);
const heap = new MinHeap();

for (let i = 1; i <= N; i++) {
    const number = parseInt(input[i]);
    heap.heapPush(number);
}

let answer = 0;
while (heap.arr.length > 2) {
    let tempSums = 0;
    tempSums += heap.heapPop();
    tempSums += heap.heapPop();
    heap.heapPush(tempSums);
    answer += tempSums;
}

console.log(answer);
