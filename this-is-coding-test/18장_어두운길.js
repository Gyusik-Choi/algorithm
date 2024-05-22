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
  // 정점 N, 간선 N - 1
  // 임의의 출발점에서 시작
  // 모든 정점들을 최소 비용으로 연결
  const mst = new Array(N).fill(false);
  const distances = new Array(N).fill(Infinity);
  distances[0] = 0;

  // let cnt = 0;
  let minDistances = 0;

  const minHeap = new MinHeap();

  minHeap.heapPush([0, 0]);

  while (minHeap.arr.length > 1) {
    const [startDist, startIdx] = minHeap.heapPop();

    if (mst[startIdx]) {
      continue;
    }

    mst[startIdx] = true;
    minDistances += startDist;

    // roads 는 
    // MinHeap 의 arr 과 달리
    // 위치, 거리 순서임을 주의
    for (const [endIdx, endDist] of roads[startIdx]) {
      if (!mst[endIdx] && distances[endIdx] > endDist) {
        distances[endIdx] = endDist;
        minHeap.heapPush([distances[endIdx], endIdx]);
      }
    }
  }

  return minDistances;
}

const input = [
  '7 11',
  '0 1 7',
  '0 3 5',
  '1 2 8',
  '1 3 9',
  '1 4 7',
  '2 4 5',
  '3 4 15',
  '3 5 6',
  '4 5 8',
  '4 6 9',
  '5 6 11',
];

const [N, M] = input.shift().split(' ').map(v => parseInt(v));
const roads = {};

for (let i = 0; i < N; i++) {
  roads[i] = [];
}

let totalDistance = 0;

input.forEach(v => {
  const [X, Y, Z] = v.split(' ').map(v => parseInt(v));

  totalDistance += Z;

  roads[X].push([Y, Z]);
  roads[Y].push([X, Z]);
});

// 절약한 비용을 구하는 문제라서
// mstPrim 의 값을 출력 하는게 아니라
// 총 비용에서 mstPrim 의 값을 빼서
// 얼마를 절약했는지 출력해야 한다
console.log(totalDistance - mstPrim());
