class MinHeap {
  constructor() {
    // 거리, y, x
    this.arr = [[-1, -1, -1]];
  }

  heapPush(lst) {
    this.arr.push(lst);

    let idx = this.arr.length - 1;

    while (idx > 1) {
      const parentIdx = Math.floor(idx / 2);

      if (this.isBigger(parentIdx, idx)) {
        this.change(parentIdx, idx);
        idx = parentIdx;
      } else {
        break;
      }
    }
  }

  isBigger(parentIdx, idx) {
    if (this.arr[parentIdx][0] > this.arr[idx][0]) {
      return true;
    }

    if (this.arr[parentIdx][0] === this.arr[idx][0]) {
      if (this.arr[parentIdx][1] > this.arr[idx][1]) {
        return true;
      }

      if (this.arr[parentIdx][1] === this.arr[idx][1]) {
        if (this.arr[parentIdx][2] > this.arr[idx][2]) {
          return true;
        }
      }
    }

    return false;
  }

  change(parentIdx, idx) {
    const temp = this.arr[parentIdx];
    this.arr[parentIdx] = this.arr[idx];
    this.arr[idx] = temp;
  }

  heapPop() {
    if (this.arr.length > 1) {
      this.change(1, this.arr.length - 1);
      const lst = this.arr.pop();
      this.heapify(1);
      return lst;
    }

    return [];
  }

  heapify(idx) {
    let parentIdx = idx;
    const leftChildIdx = parentIdx * 2;
    const rightChildIdx = parentIdx * 2 + 1;

    if (this.arr.length > leftChildIdx && this.isBigger(parentIdx, leftChildIdx)) {
      parentIdx = leftChildIdx;
    }

    if (this.arr.length > rightChildIdx && this.isBigger(parentIdx, rightChildIdx)) {
      parentIdx = rightChildIdx;
    }

    if (parentIdx !== idx) {
      this.change(parentIdx, idx);
      return this.heapify(parentIdx);
    }
  }
}

const move = () => {
  let time = 0;
  let sharkSize = 2;
  let cnt = 0;

  while (true) {
    const shark = findShark();

    const fish = findFish(shark, sharkSize);

    if (fish.length === 0) {
      break;
    }

    time += fish.shift();

    moveShark(shark, fish);

    cnt += 1;

    if (sharkSize === cnt) {
      sharkSize += 1;
      cnt = 0;
    }
  }

  return time;
}

const findShark = () => {
  for (let i = 0; i < N; i++) {
    for (let j = 0; j < N; j++) {
      if (spaces[i][j] === 9) {
        return [i, j];
      }
    }
  }
}

// 가장 우선 순위의 물고기 한 마리
const findFish = (sharkIdx, size) => {
  let minTime = Infinity;
  
  const shark = [0, ...sharkIdx];

  const minHeap = new MinHeap();

  const copiedSpace = copySpace(spaces);

  copiedSpace[shark[1]][shark[2]] = -1;
  
  const q = [shark];

  let idx = 0;

  const yValue = [-1, 0, 1, 0];
  const xValue = [0, 1, 0, -1];

  while (q.length > idx) {
    const [time, y, x] = q[idx];

    idx += 1;

    if (time > minTime) {
      break;
    }

    for (let i = 0; i < 4; i++) {
      const [yIdx, xIdx] = [y + yValue[i], x + xValue[i]];

      if (0 > yIdx || yIdx >= N || 0 > xIdx || xIdx >= N) {
        continue;
      }

      if (copiedSpace[yIdx][xIdx] === -1) {
        continue;
      }
      
      if (copiedSpace[yIdx][xIdx] <= size) {
        q.push([time + 1, yIdx, xIdx]);

        if (0 < copiedSpace[yIdx][xIdx] && copiedSpace[yIdx][xIdx] < size) {
          minTime = time;

          minHeap.heapPush([time + 1, yIdx, xIdx]);
        }

        copiedSpace[yIdx][xIdx] = -1;
      }
    }
  }

  return minHeap.heapPop();
}

const copySpace = (space) => {
  const copiedSpace = [];

  for (let i = 0; i < N; i++) {
    const tempSpace = [];

    for (let j = 0; j < N; j++) {
      tempSpace.push(space[i][j]);
    }

    copiedSpace.push(tempSpace);
  }

  return copiedSpace;
}

const moveShark = (shark, fish) => {
  // 상어 위치는 0
  // 물고기 위치는 9
  spaces[shark[0]][shark[1]] = 0;
  spaces[fish[0]][fish[1]] = 9;
}

// const fs = require('fs');
// const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

// const input = [
//   '3',
//   '0 0 0',
//   '0 0 0',
//   '0 9 0',
// ];
// => 0

// const input = [
//   '3',
//   '0 0 1',
//   '0 0 0',
//   '0 9 0',
// ];
// => 3

const input = [
  '4',
  '4 3 2 1',
  '0 0 0 0',
  '0 0 9 0',
  '1 2 3 4',
];
// => 14

// const input = [
//   '6',
//   '5 4 3 2 3 4',
//   '4 3 2 3 4 5',
//   '3 2 9 5 6 6',
//   '2 1 2 3 4 5',
//   '3 2 1 6 5 4',
//   '6 6 6 6 6 6',
// ];
// => 60

// const input = [
//   '6',
//   '6 0 6 0 6 1',
//   '0 0 0 0 0 2',
//   '2 3 4 5 6 6',
//   '0 0 0 0 0 2',
//   '0 2 0 0 0 0',
//   '3 9 3 0 0 1',
// ];
// => 48

// const input = [
//   '6',
//   '1 1 1 1 1 1',
//   '2 2 6 2 2 3',
//   '2 2 5 2 2 3',
//   '2 2 2 4 6 3',
//   '0 0 0 0 0 6',
//   '0 0 0 0 0 9',
// ];
// => 39

const N = parseInt(input.shift());

const spaces = input.map(v => v.split(' ').map(v => parseInt(v)));

console.log(move());

// 우선 순위 큐 활용하기
