class MinHeap {
    constructor() {
        this.arr = [[0, 0]];
    }

    switch(i, j) {
        const temp = this.arr[i];
        this.arr[i] = this.arr[j];
        this.arr[j] = temp;
    }

    heapPush(number) {
        this.arr.push(number);

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

    heapPop() {
        this.switch(1, this.arr.length - 1);
        const popedItem = this.arr.pop();
        this.heapify(1);
        return popedItem;
    }

    heapify(idx) {
        let parentIdx = idx;
        const leftChildIdx = parentIdx * 2
        const rightChildIdx = leftChildIdx + 1;

        // this.arr[parentIdx] > this.arr[leftChildIdx] 로 비교해서 처음에 오답이 나왔다
        if (this.arr.length > leftChildIdx && this.arr[parentIdx][0] > this.arr[leftChildIdx][0]) {
            parentIdx = leftChildIdx;
        }

        // this.arr[parentIdx] > this.arr[rightChildIdx] 로 비교해서 처음에 오답이 나왔다
        if (this.arr.length > rightChildIdx && this.arr[parentIdx][0] > this.arr[rightChildIdx][0]) {
            parentIdx = rightChildIdx;
        }

        if (parentIdx != idx) {
            this.switch(idx, parentIdx);
            this.heapify(parentIdx);
        }
    }
}

const linearSearch = (minHeap, k) => {
    minHeap.arr.shift();
    const newSortedFoodTimes = minHeap.arr.sort(sortCallBack);
    return newSortedFoodTimes[k % minHeap.arr.length][1];
}

const eat = (minHeap, previousFood) => {
    const firstFood = minHeap.arr[1][0];
    return (firstFood - previousFood) * (minHeap.arr.length - 1);
}

const eatFood = (minHeap, k) => {
    let previousFood = 0;
    
    while (eat(minHeap, previousFood) < k) {
        k -= eat(minHeap, previousFood);
        const firstFood = minHeap.heapPop();
        previousFood = firstFood[0];
    }

    // 선형탐색
    return linearSearch(minHeap, k);
}

const sortCallBack = (a, b) => {
    if (a[1] === b[1]) {
        return a[0] - b[0];
    }

    return a[1] - b[1];
}

const sums = (foodTimes) => {
    return foodTimes.reduce((acc, cur) => acc + cur);
}

const solution = (foodTimes, k) => {
    if (sums(foodTimes) <= k) {
        return -1;
    }

    // [[값, 인덱스] ... ]
    const minHeap = new MinHeap();
    // heap 에 넣을 때 인덱스 + 1 한다
    foodTimes.forEach((v, i) => minHeap.heapPush([v, i + 1]));
    return eatFood(minHeap, k);
}

console.log(solution([3, 1, 2], 5));
// 1
console.log(solution([2, 3, 1, 5, 4], 3));
// 4
console.log(solution([1, 2, 3, 4], 4));
// 1
console.log(solution([1, 1, 1, 1, 1, 1], 1));
// 2
console.log(solution([1, 100], 10));
// 2
console.log(solution([3, 1, 1, 1, 2, 4, 3], 12));
// 6
console.log(solution([4, 3, 5, 6, 2], 7));
// 3
console.log(solution([4, 1, 1, 5], 4));
// 1
console.log(solution([2, 2, 2], 4));
// 2
console.log(solution([2, 2, 2], 1));
// 2
