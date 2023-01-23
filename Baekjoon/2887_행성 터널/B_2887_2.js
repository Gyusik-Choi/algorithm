class MinHeap {
  constructor() {
    // 거리, 정점
    this.arr = [[-1, -1]];
  }

  heapPush(lst) {
    this.arr.push(lst);

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

  change(a, b) {
    const temp = this.arr[a];
    this.arr[a] = this.arr[b];
    this.arr[b] = temp;
  }

  heapPop() {
    if (this.arr.length > 0) {
      this.change(1, this.arr.length - 1);
      const popedArr = this.arr.pop();
      this.heapify(1);
      return popedArr;
    }
  }

  heapify(idx) {
    let parentIdx = idx;
    const leftChildIdx = parentIdx * 2;
    const rightChildIdx = parentIdx * 2 + 1;

    if (this.arr.length > leftChildIdx && this.arr[parentIdx][0] > this.arr[leftChildIdx][0]) {
      parentIdx = leftChildIdx;
    }

    if (this.arr.length > rightChildIdx && this.arr[parentIdx][0] > this.arr[rightChildIdx][0]) {
      parentIdx = rightChildIdx;
    }

    if (parentIdx !== idx) {
      this.change(idx, parentIdx);
      return this.heapify(parentIdx);
    }
  }
}

const mstPrim = () => {
  const mst = new Array(N).fill(false);
  const distances = new Array(N).fill(Infinity);

  distances[0] = 0;

  let minDistances = 0;

  const minHeap = new MinHeap();

  minHeap.heapPush([0, 0]);

  while (minHeap.arr.length > 1) {
    const [startDist, start] = minHeap.heapPop();

    if (mst[start]) {
      continue;
    }

    mst[start] = true;
    minDistances += startDist;

    for (let end = 0; end < N; end++) {
      if (start !== end && planets[start][end] !== Infinity) {
        if (!mst[end] && distances[end] > planets[start][end]) {
          distances[end] = planets[start][end];

          minHeap.heapPush([distances[end], end]);
        }
      }
    }
  }

  return minDistances;
}

const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

// const input = [
//   '5',
//   '11 -15 -15',
//   '14 -5 -15',
//   '-1 -1 -5',
//   '10 -4 -1',
//   '19 -4 19',
// ];

const N = parseInt(input[0]);

const xPlanets = [];
const yPlanets = [];
const zPlanets = [];

for (let i = 0; i < N; i++) {
  const [x, y, z] = input[i + 1].split(' ').map(v => parseInt(v));

  xPlanets.push([x, i]);
  yPlanets.push([y, i]);
  zPlanets.push([z, i]);
}

// 좌표 기준으로 정렬
xPlanets.sort((a, b) => a[0] - b[0]);
yPlanets.sort((a, b) => a[0] - b[0]);
zPlanets.sort((a, b) => a[0] - b[0]);

const planets = new Array(N).fill(Infinity).map(v => new Array(N).fill(Infinity));

for (let i = 0; i < N - 1; i++) {
  planets[xPlanets[i][1]][xPlanets[i + 1][1]] = Math.min(planets[xPlanets[i][1]][xPlanets[i + 1][1]], xPlanets[i + 1][0] - xPlanets[i][0]);
  planets[xPlanets[i + 1][1]][xPlanets[i][1]] = Math.min(planets[xPlanets[i + 1][1]][xPlanets[i][1]], xPlanets[i + 1][0] - xPlanets[i][0]);

  planets[yPlanets[i][1]][yPlanets[i + 1][1]] = Math.min(planets[yPlanets[i][1]][yPlanets[i + 1][1]], yPlanets[i + 1][0] - yPlanets[i][0]);
  planets[yPlanets[i + 1][1]][yPlanets[i][1]] = Math.min(planets[yPlanets[i + 1][1]][yPlanets[i][1]], yPlanets[i + 1][0] - yPlanets[i][0]);

  planets[zPlanets[i][1]][zPlanets[i + 1][1]] = Math.min(planets[zPlanets[i][1]][zPlanets[i + 1][1]], zPlanets[i + 1][0] - zPlanets[i][0]);
  planets[zPlanets[i + 1][1]][zPlanets[i][1]] = Math.min(planets[zPlanets[i + 1][1]][zPlanets[i][1]], zPlanets[i + 1][0] - zPlanets[i][0]);
}

console.log(mstPrim());
