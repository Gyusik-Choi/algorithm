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
  // distances 배열을 안 쓰는 방법을 B_2887_2 에서 했으나
  // 메모리나 시간 면에서 distances 를 사용하는 해당 방법이 모두 더 나았다
  const distances = new Array(N).fill(Infinity);
  let minDistances = 0;

  distances[0] = 0;

  const minHeap = new MinHeap();

  minHeap.heapPush([0, 0]);

  while (minHeap.arr.length > 1) {
    const [startDist, start] = minHeap.heapPop();

    if (mst[start]) {
      continue;
    }

    mst[start] = true;
    minDistances += startDist;

    for (const [end, endDist] of planets[start]) {
      if (!mst[end] && distances[end] > endDist) {
        distances[end] = endDist;
        minHeap.heapPush([endDist, end]);
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

const planets = {};

for (let i = 0; i < N; i++) {
  planets[i] = [];
}

// B_2887(메모리초과) 파일과 달리
// 대소비교를 하지 않고
// 한 시작 정점으로부터 다른 도착 정점에 값이 두개 이상 들어갈지라도
// 일단 넣어주고
// heap 에서 비교를 통해 처리하도록 한다
for (let i = 0; i < N - 1; i++) {
  planets[xPlanets[i][1]].push([xPlanets[i + 1][1], xPlanets[i + 1][0] - xPlanets[i][0]]);
  planets[xPlanets[i + 1][1]].push([xPlanets[i][1], xPlanets[i + 1][0] - xPlanets[i][0]]);

  planets[yPlanets[i][1]].push([yPlanets[i + 1][1], yPlanets[i + 1][0] - yPlanets[i][0]]);
  planets[yPlanets[i + 1][1]].push([yPlanets[i][1], yPlanets[i + 1][0] - yPlanets[i][0]]);

  planets[zPlanets[i][1]].push([zPlanets[i + 1][1], zPlanets[i + 1][0] - zPlanets[i][0]]);
  planets[zPlanets[i + 1][1]].push([zPlanets[i][1], zPlanets[i + 1][0] - zPlanets[i][0]]);
}

console.log(mstPrim());
