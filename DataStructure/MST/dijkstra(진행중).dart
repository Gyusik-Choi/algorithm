// 최소힙으로 구현
class Heap {
  List<List<int>> arr = [[0]];

  void heapPush(List<int> number) {
    arr.add(number);

    int idx = arr.length - 1;
    while (idx > 1) {
      int parentIdx = idx ~/ 2;
      
      if (arr[parentIdx][0] > arr[idx][0]) {
        List<int> temp = arr[idx];
        arr[idx] = arr[parentIdx];
        arr[parentIdx] = temp;
        idx ~/= 2;
      } else {
        break;
      }
    }
  }

  List<int> heapPop() {
    if (arr.length < 2) {
      return [];
    }

    if (arr.length < 3) {
      return arr.removeLast();
    }

    List<int> temp = arr[arr.length - 1];
    arr[arr.length - 1] = arr[1];
    arr[1] = temp;

    heapify(1);
    return arr.removeLast();
  }

  void heapify(int idx) {
    int parentIdx = idx;
    int leftChildIdx = idx * 2;
    int rightChildIdx = idx * 2 + 1;

    if (leftChildIdx < arr.length) {
      if (arr[parentIdx][0] > arr[leftChildIdx][0]) {
        parentIdx = leftChildIdx;
      }
    }

    if (rightChildIdx < arr.length) {
      if (arr[parentIdx][0] > arr[rightChildIdx][0]) {
        parentIdx = rightChildIdx;
      }
    }

    if (idx != parentIdx) {
      List<int> temp = arr[idx];
      arr[idx] = arr[parentIdx];
      arr[parentIdx] = temp;
      return heapify(parentIdx);
    }
  }
}

List<int> dijksra(int n, Map<int, List<List<int>>> nodes) {
  List<bool> selected = [];
  for (int i = 0; i < n; i++) {
    selected.add(false);
  }


  List<int> distances = [];
  int maxNum = 10000;
  for (int i = 0; i < n; i++) {
    distances.add(maxNum);
  }

  distances[0] = 0;

  Heap minHeap = Heap();
  minHeap.heapPush([0, 0]);

  while (minHeap.arr.length > 1) {
    print(minHeap.arr);
    List<int> popedNum = minHeap.heapPop();
    int start = popedNum[1];

    if (selected[start]) {
      continue;
    }

    selected[start] = true;

    if (nodes[start] != null) {
      for (int i = 0; i < nodes[start]!.length; i++) {
        List<int> endNode = nodes[start]![i];
        int end = endNode[0];
        int value = endNode[1];

        if (!selected[end]) {
          if (distances[end] > distances[start] + value) {
            distances[end] = distances[start] + value;
            minHeap.heapPush([distances[end], end]);
          }
        }
      }
    }
  }

  return distances;
}

void main() {
  int N = 6;
  // int M = 11;

  Map<int, List<List<int>>> nodes = Map();
  
  List<List<int>> endAndDistances = [
    [0, 1, 3], 
    [0, 2, 5], 
    [1, 2, 2], 
    [1, 3, 6], 
    [2, 1, 1], 
    [2, 3, 4], 
    [2, 4, 6], 
    [3, 4, 2], 
    [3, 5, 3], 
    [4, 0, 3], 
    [4, 5, 6],
  ];

  for (int i = 0; i < endAndDistances.length; i++) {
    List<int> endAndDistance = endAndDistances[i];
    int key = endAndDistance[0];

    if (!nodes.containsKey(key)) {
      nodes[key] = [[endAndDistance[1], endAndDistance[2]]];
    } else {
      nodes[key]!.add([endAndDistance[1], endAndDistance[2]]);
    }
  }

  List<int> answer = dijksra(N, nodes);
  print(answer);
}


// 6 11
// 0 1 3
// 0 2 5
// 1 2 2
// 1 3 6
// 2 1 1
// 2 3 4
// 2 4 6
// 3 4 2
// 3 5 3
// 4 0 3
// 4 5 6