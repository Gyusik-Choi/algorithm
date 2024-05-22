class MinHeap {
  constructor() {
    this.arr = [[-1, -1]];
  }

  heapPush(number) {
    this.arr.push(number);

    let idx = this.arr.length - 1;

    while (idx > 1) {
      const parentIdx = Math.floor(idx / 2);

      if (this.arr[parentIdx][0] > this.arr[idx][0]) {
        this.change(parentIdx, idx);
        idx = parentIdx;
      } else {
        break;
      }
    }
  }

  change(idx1, idx2) {
    const temp = this.arr[idx1];
    this.arr[idx1] = this.arr[idx2];
    this.arr[idx2] = temp;
  }

  heapPop() {
    this.change(1, this.arr.length - 1);
    const popedNumber = this.arr.pop();
    this.heapify(1);
    return popedNumber;
  }

  heapify(idx) {
    let parentIdx = idx;
    let leftChildIdx = parentIdx * 2;
    let rightChildIdx = parentIdx * 2 + 1;

    if (this.arr.length > leftChildIdx && this.arr[parentIdx][0] > this.arr[leftChildIdx][0]) {
      parentIdx = leftChildIdx;
    }

    if (this.arr.length > rightChildIdx && this.arr[parentIdx][0] > this.arr[rightChildIdx][0]) {
      parentIdx = rightChildIdx;
    }

    if (parentIdx !== idx) {
      // 처음에 여기서 교환을 하지 않아서 답을 구할 수 없었다
      this.change(parentIdx, idx);
      return this.heapify(parentIdx);
    }
  }
}

const dijkstra = (n, obj, costsInfo) => {
  const minHeap = new MinHeap();

  minHeap.heapPush([costsInfo[0][0], 0]);

  const visited = new Array(n * n).fill(false);
  const distances = new Array(n * n).fill(Infinity);

  distances[0] = costsInfo[0][0];

  while (minHeap.arr.length > 1) {
    const [startDist, start] = minHeap.heapPop();

    if (visited[start]) {
      continue;
    }

    visited[start] = true;

    if (obj[start] !== undefined) {
      for (const [endDist, end] of obj[start]) {
        if (!visited[end]) {
          if (startDist + endDist < distances[end]) {
            distances[end] = startDist + endDist;
            minHeap.heapPush([distances[end], end]);
          }
        }
      }
    }
  }

  return distances[n * n - 1];
}

const setCostsObj = (costsInfo) => {
  const n = costsInfo.length;

  const obj = {};

  for (let i = 0; i < n * n; i++) {
    obj[i] = [];
  }

  const yValue = [-1, 0, 1, 0];
  const xValue = [0, 1, 0, -1];

  for (let i = 0; i < n; i++) {
    for (let j = 0; j < n; j++) {
      for (let k = 0; k < 4; k++) {
        const y = yValue[k] + i;
        const x = xValue[k] + j

        if (0 > y || y >= n || 0 > x || x >= n) {
          continue;
        }

        // 거리, 위치
        obj[i * n + j].push([costsInfo[y][x], y * n + x]);
      }
    }
  }

  return obj;
}

const input = [
'3',
'3',
'5 5 4',
'3 9 1',
'3 2 7',
'5',
'3 7 2 0 1',
'2 8 0 9 1',
'1 2 1 8 1',
'9 8 9 2 0',
'3 6 5 1 5',
'7',
'9 0 5 1 1 5 3',
'4 1 2 1 6 5 3',
'0 7 6 1 6 8 5',
'1 1 7 8 3 2 3',
'9 4 0 7 6 4 1',
'5 8 3 2 4 8 3',
'7 4 8 4 8 3 4',
];

// const input = [
//   '1',
//   '3',
//   '5 5 4',
//   '3 9 1',
//   '3 2 7',
// ];

// const input = [
//   '1',
//   '5',
//   '3 7 2 0 1',
//   '2 8 0 9 1',
//   '1 2 1 8 1',
//   '9 8 9 2 0',
//   '3 6 5 1 5',
// ];

// const input = [
//   '1',
//   '7',
//   '9 0 5 1 1 5 3',
//   '4 1 2 1 6 5 3',
//   '0 7 6 1 6 8 5',
//   '1 1 7 8 3 2 3',
//   '9 4 0 7 6 4 1',
//   '5 8 3 2 4 8 3',
//   '7 4 8 4 8 3 4',
// ];

const T = parseInt(input.shift());

for (let i = 0; i < T; i++) {
  const N = parseInt(input.shift());
  const costs = [];

  for (let j = 0; j < N; j++) {
    costs.push(input.shift().split(' ').map(v => parseInt(v)));
  }

  const costsObj = setCostsObj(costs);

  console.log(dijkstra(N, costsObj, costs));
}
