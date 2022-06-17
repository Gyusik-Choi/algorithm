class Heap {
  List<int> arr = [0];

  void heapPush(int number) {
    arr.add(number);
    int idx = arr.length - 1;

    while (idx > 1) {
      int parentIdx = idx ~/ 2;

      if (arr[parentIdx] > arr[idx]) {
        int temp = arr[idx];
        arr[idx] = arr[parentIdx];
        arr[parentIdx] = temp;
        idx ~/= 2;
      } else {
        break;
      }
    }
  }

  int heapPop() {
    if (arr.length < 2) {
      return -1;
    }

    if (arr.length < 3) {
      return arr.removeAt(1);
    }

    int temp = arr[arr.length - 1];
    arr[arr.length - 1] = arr[1];
    arr[1] = temp;

    int popedNumber = arr.removeLast();
    heapify(1);
    return popedNumber;
  }

  void heapify(int idx) {
    int parentIdx = idx;
    int leftChildIdx = idx * 2;
    int rightChildIdx = idx * 2 + 1;

    if (leftChildIdx < arr.length) {
      if (arr[parentIdx] > arr[leftChildIdx]) {
        parentIdx = leftChildIdx;
      }
    }

    if (rightChildIdx < arr.length) {
      if (arr[parentIdx] > arr[rightChildIdx]) {
        parentIdx = rightChildIdx;
      }
    }

    if (idx != parentIdx) {
      int temp = arr[idx];
      arr[idx] = arr[parentIdx];
      arr[parentIdx] = temp;
      return heapify(parentIdx);
    }
  }
}

void main() {
  Heap minHeap = Heap();
  minHeap.heapPush(10);
  minHeap.heapPush(9);
  minHeap.heapPush(8);
  minHeap.heapPush(7);
  minHeap.heapPush(6);
  minHeap.heapPush(5);
  minHeap.heapPush(4);
  minHeap.heapPush(3);
  minHeap.heapPush(2);
  minHeap.heapPush(1);
  print(minHeap.heapPop());
  print(minHeap.heapPop());
  print(minHeap.heapPop());
  print(minHeap.heapPop());
  print(minHeap.heapPop());
  print(minHeap.heapPop());
  print(minHeap.heapPop());
  print(minHeap.heapPop());
  print(minHeap.heapPop());
  print(minHeap.heapPop());
}