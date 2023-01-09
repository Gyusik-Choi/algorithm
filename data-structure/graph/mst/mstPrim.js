// 이것이 코딩테스트다 어두운길 문제 풀이 + MST Prim (+ Heap) 구현

class MinHeap {
    constructor() {
        this.arr = [[0, 0]];
    }

    heapPush(roadInfo) {
        this.arr.push(roadInfo);

        let idx = this.arr.length - 1;
        while (idx > 1) {
            const parentIdx = parseInt(idx / 2);

            if (this.arr[parentIdx][0] > this.arr[idx][0]) {
                this.switch(parentIdx, idx);
                idx = parentIdx;
            } else {
                break;
            }
        }
    }

    switch(first, second) {
        const temp = this.arr[first];
        this.arr[first] = this.arr[second];
        this.arr[second] = temp;
    }

    heapPop() {
        this.switch(1, this.arr.length - 1);
        const popedRoadInfo = this.arr.pop();
        this.heapify(1);
        return popedRoadInfo;
    }

    heapify(idx) {
        let parentIdx = idx;
        const leftChildIdx = parentIdx * 2;
        const rightChildIdx = parentIdx * 2 + 1;

        if (leftChildIdx < this.arr.length) {
            if (this.arr[parentIdx][0] > this.arr[leftChildIdx][0]) {
                parentIdx = leftChildIdx;
            }
        }

        if (rightChildIdx < this.arr.length) {
            if (this.arr[parentIdx][0] > this.arr[rightChildIdx][0]) {
                parentIdx = rightChildIdx;
            }
        }

        if (idx != parentIdx) {
            this.switch(idx, parentIdx);
            return this.heapify(parentIdx);
        }
    }
}

class MstPrim {
    constructor(n) {
        this.mst = new Array(n + 1).fill(false);
        this.distance = new Array(n + 1).fill(Infinity);
    }

    getSums() {
        let sums = 0;
        // 0 번 지점을 시작 위치로 설정
        this.distance[0] = 0;

        const minHeap = new MinHeap();
        // 거리, 시작점
        minHeap.heapPush([0, 0]);

        while (minHeap.arr.length > 1) {
            const [startDist, start] = minHeap.heapPop();

            if (this.mst[start]) {
                continue;
            }

            this.mst[start] = true;
            sums += startDist;

            for (let i = 0; i < roads[start].length; i++) {
                const [dist, end] = roads[start][i];
                
                if (!this.mst[end] && this.distance[end] > dist) {
                    this.distance[end] = dist;
                    minHeap.heapPush([this.distance[end], end]);
                }
            }
        }

        return sums;
    }
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
]

const N = parseInt(input[0][0]);
const M = parseInt(input[0][1]);

const roads = new Array(N).fill(0).map(v => new Array());
let total = 0;
for (let i = 1; i < input.length; i++) {
    const [X, Y, Z] = input[i].split(' ').map(v => parseInt(v));
    roads[X].push([Z, Y]);
    roads[Y].push([Z, X]);
    total += Z;
}

const mstPrim = new MstPrim(N);
console.log(total - mstPrim.getSums());
