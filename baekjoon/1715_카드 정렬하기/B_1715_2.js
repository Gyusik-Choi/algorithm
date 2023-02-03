class MinHeap {
  constructor() {
    this.arr = [0];
  }

  change(a, b) {
    const temp = this.arr[a];
    this.arr[a] = this.arr[b];
    this.arr[b] = temp;
  }

  heapPush(number) {
    this.arr.push(number);

    let idx = this.arr.length - 1;

    while (idx > 1) {
      const parentIdx = Math.floor(idx / 2);

      if (this.arr[parentIdx] > this.arr[idx]) {
        this.change(parentIdx, idx);
        idx = parentIdx;
      } else {
        break;
      }
    }
  }

  heapPop() {
    this.change(1, this.arr.length - 1);
    const popedNumber = this.arr.pop();
    this.heapify(1);
    return popedNumber;
  }

  heapify(idx) {
    let parentIdx = idx;
    const leftChildIdx = parentIdx * 2;
    const rightChildIdx = parentIdx * 2 + 1;

    if (this.arr.length > leftChildIdx && this.arr[parentIdx] > this.arr[leftChildIdx]) {
      parentIdx = leftChildIdx;
    }

    if (this.arr.length > rightChildIdx && this.arr[parentIdx] > this.arr[rightChildIdx]) {
      parentIdx = rightChildIdx;
    }

    if (idx !== parentIdx) {
      this.change(idx, parentIdx);
      return this.heapify(parentIdx);
    }
  }
}

const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

// const input = [
//   '3',
//   '10',
//   '20',
//   '40'
// ];
// => 100

// const input = [
//   '4',
//   '40',
//   '10',
//   '20',
//   '30'
// ];
// => 190

// const input = [
//   '5',
//   '10',
//   '50',
//   '30',
//   '40',
//   '20',
// ];
// => 330

// const input = [
//   '1',
//   '10',
// ];
// => 0

const N = parseInt(input[0]);
input.shift();

const numbers = input.map(v => parseInt(v));
const minHeap = new MinHeap();
numbers.forEach(v => minHeap.heapPush(v));

let sums = 0;

// 최소 비교 횟수를 구하는 문제다
// 이 문제에서 비교 횟수는 
// 비교가 이뤄졌을 때
// 비교하는 두 숫자의 합이라서
// N 이 1 이면 비교가 일어나지 않기 때문에
// 정답은 0이 된다
while (minHeap.arr.length > 2) {
  const first = minHeap.heapPop();
  const second = minHeap.heapPop();
  const tempSums = first + second;

  sums += tempSums;
  minHeap.heapPush(tempSums);
}

console.log(sums);
