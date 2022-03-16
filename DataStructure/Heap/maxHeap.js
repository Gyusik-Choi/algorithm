const Heap = function() {
    this.arr = [null];
}

// 힙에 추가
Heap.prototype.heapPush = function(value) {
    this.arr.push(value);
    
    let idx = this.arr.length - 1;
    while (idx > 1) {
        const parentIdx = Math.floor(idx / 2);
           
        // 자식 노드 값이 부모 노드 값보다 크면 교환
        // 상위 노드를 더 탐색할 수 있도록 idx 에서 2를 나눠준다
        if (this.arr[parentIdx] < this.arr[idx]) {
            const temp = this.arr[idx];
            this.arr[idx] = this.arr[parentIdx];
            this.arr[parentIdx] = temp;

            idx = Math.floor(idx / 2);
        
        // 자식 노드 값이 부모 노드 값보다 작으면 종료
        } else {
            break;
        }
    }
}

// 힙에서 최대값 찾기 + maxHeapify 함수 호출하여 힙 재정렬
Heap.prototype.heapPop = function() {
    // 힙의 마지막 요소
    const maxIdx = this.arr.length - 1;

    // 힙의 첫번째 요소와 마지막 요소를 교환
    const temp = this.arr[1];
    this.arr[1] = this.arr[maxIdx];
    this.arr[maxIdx] = temp;

    // 교환 후 기존에 힙의 첫번째 요소였던 마지막 요소를 힙에서 제거
    // 기존에 힙의 맨 마지막 요소였던 첫번째 요소의 올바른 위치를 찾기 위해 maxHeapify 함수 호출
    const popItem = this.arr.pop()
    this.maxHeapify(1);
    console.log(popItem);
    return popItem;
}

// 힙 재정렬
Heap.prototype.maxHeapify = function(idx) {
    let parentIdx = idx;
    const leftChildIdx = idx * 2;
    const rightChildIdx = idx * 2 + 1;

    // 왼쪽 자식 노드가 힙의 길이보다 길면 힙의 최대 인덱스를 벗어나서 잘못된 인덱스다
    if (leftChildIdx < this.arr.length && this.arr[parentIdx] < this.arr[leftChildIdx]) {
        parentIdx = leftChildIdx;
    }

    // 오른쪽 자식 노드가 힙의 길이보다 길면 힙의 최대 인덱스를 벗어나서 잘못된 인덱스다
    if (rightChildIdx < this.arr.length && this.arr[parentIdx] < this.arr[rightChildIdx]) {
        parentIdx = rightChildIdx;
    }

    // 파라미터인 idx와 기존에 idx 값을 받은 parentIdx가 같지 않다는 것은
    // parentIdx의 값이 왼쪽 자식 노드나 오른쪽 자식 노드의 인덱스 값으로 바뀌었다는 것이고
    // 이는 자식 노드에서 부모 노드보다 더 큰 값이 있다는 것이다
    // parentIdx는 왼쪽과 오른쪽 중에서 서로 간에 더 크고 부모 노드보다 더 큰 자식 노드의 인덱스를 갖는다 
    // idx 인덱스의 값(부모 노드)와 parentIdx 인덱스의 값(자식 노드 - 왼쪽과 오른쪽 중에서 더 크면서 부모 보다 큰 노드)를 교환
    // 힙의 마지막까지 탐색할 수 있도록 재귀적으로 maxHeapify 함수를 호출한다
    if (parentIdx !== idx) {
        const temp = this.arr[idx];
        this.arr[idx] = this.arr[parentIdx];
        this.arr[parentIdx] = temp;

        return this.maxHeapify(parentIdx);
    }
}

const heap = new Heap();
heap.heapPush(1);
heap.heapPush(2);
heap.heapPush(3);
heap.heapPush(4);
heap.heapPush(5);
heap.heapPush(6);
heap.heapPush(7);
heap.heapPush(8);
heap.heapPush(9);
heap.heapPush(10);
heap.heapPop();
heap.heapPop();
heap.heapPop();
heap.heapPop();
heap.heapPop();
heap.heapPop();
heap.heapPop();
heap.heapPop();
heap.heapPop();
heap.heapPop();
console.log(heap.arr);
