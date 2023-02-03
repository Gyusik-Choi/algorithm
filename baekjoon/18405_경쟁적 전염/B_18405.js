class Heap {
  constructor() {
    this.arr = [[-1]];
  }

  heapPush(number) {
    this.arr.push(number);

    let idx = this.arr.length - 1;
    
    while (idx > 1) {
      const parentIdx = parseInt(idx / 2);

      if (this.arr[parentIdx][0] > this.arr[idx][0]) {
        this.#switchValue(parentIdx, idx);
        idx = parentIdx;
      } else {
        break;
      }
    }
  }

  // private method
  #switchValue(a, b) {
    const temp = this.arr[a];
    this.arr[a] = this.arr[b];
    this.arr[b] = temp;
  }

  heapPop() {
    this.#switchValue(1, this.arr.length - 1);
    const popedNumber = this.arr.pop();
    this.heapify(1);
    return popedNumber;
  }

  heapify(idx) {
    let parentIdx = idx;
    const leftChildIdx = idx * 2;
    const rightChildIDx = idx * 2 + 1;
    
    if (leftChildIdx < this.arr.length && this.arr[parentIdx][0] > this.arr[leftChildIdx][0]) {
      parentIdx = leftChildIdx;
    }

    if (rightChildIDx < this.arr.length && this.arr[parentIdx][0] > this.arr[rightChildIDx][0]) {
      parentIdx = rightChildIDx;
    }

    if (idx != parentIdx) {
      this.#switchValue(idx, parentIdx);
      this.heapify(parentIdx);
    }
  }
}

const isAllMoved = (maps) => {
  for (let i = 0; i < N; i++) {
    for (let j = 0; j < N; j++) {
      if (maps[i][j] === 0) {
        return false;
      }
    }
  }

  return true;
}

const putEveryVirusToHeap = (h) => {
  for (let i = 0; i < N; i++) {
    for (let j = 0; j < N; j++) {
      if (maps[i][j] !== 0) {
        // 바이러스 번호, y, x
        h.heapPush([maps[i][j], i, j]);
      }
    }
  }
}

// heap 에 0이 아닌 모든 원소들을 넣어두고
// 바이러스 이동을 진행한다
// 다 이동했을 경우에는 초가 남았더라도
// 더 이상 탐색을 하지 않는다
const moveVirus = (maps) => {
  let idx = 0;

  while (!isAllMoved(maps) && idx < S) {
    const heap = new Heap();
    putEveryVirusToHeap(heap);

    while (heap.arr.length > 1) {
      const [num, y, x] = heap.heapPop();

      const yValue = [-1, 0, 1, 0];
      const xValue = [0, 1, 0, -1];
  
      for (let i = 0; i < 4; i++) {
        const yIdx = y + yValue[i];
        const xIdx = x + xValue[i];
        
        if (0 > yIdx || yIdx >= N || 0 > xIdx || xIdx >= N) {
          continue;
        }

        if (maps[yIdx][xIdx] !== 0) {
          continue;
        }

        maps[yIdx][xIdx] = num;
      }
    }

    idx += 1;
  }
}

const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

// const input = [
//   '3 3',
//   '1 0 2',
//   '0 0 0',
//   '3 0 0',
//   '2 3 2'
// ];

// const input = [
//   '3 3',
//   '1 0 2',
//   '0 0 0',
//   '3 0 0',
//   '1 2 2'
// ];

// 행 원소 갯수, 바이러스 번호 최대값
const [N, K] = input[0].split(' ').map(v => parseInt(v));
input.shift();

// 초, y, x
const [S, X, Y] = input.pop().split(' ').map(v => parseInt(v));

const maps = input.map(v => v.split(' ').map(v => parseInt(v)));

moveVirus(maps);
console.log(maps[X - 1][Y - 1]);
