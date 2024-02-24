import 'dart:collection';

class Heap {
  List<Node> q = [Node(-1, -1)];

  void push(Node node) {
    q.add(node);

    int childIdx = q.length - 1;

    while (childIdx > 0) {
      int parentIdx = childIdx ~/ 2;

      if (q[parentIdx].distance > q[childIdx].distance) {
        Node temp = q[parentIdx];
        q[parentIdx] = q[childIdx];
        q[childIdx] = temp;

        childIdx ~/= 2;
      } else {
        break;
      }
    }
  }

  Node pop() {
    if (q.length < 2) {
      throw Error();
    }

    if (q.length < 3) {
      return q.removeLast();
    }

    int lastIdx = q.length - 1;
    Node temp = q[lastIdx];
    q[lastIdx] = q[1];
    q[1] = temp;

    // 미리 빼놓고 heapify 를 진행해야 한다
    Node val = q.removeLast();
    heapify(1);
    return val;
  }

  void heapify(int idx) {
    int parentIdx = idx;
    int leftChildIdx = idx * 2;
    int rightChildIdx = idx * 2 + 1;

    if (
      q.length > leftChildIdx && 
      q[parentIdx].distance > q[leftChildIdx].distance
    ) {
      parentIdx = leftChildIdx;
    }

    if (
      q.length > rightChildIdx && 
      q[parentIdx].distance > q[rightChildIdx].distance
    ) {
      parentIdx = rightChildIdx;
    }

    if (idx != parentIdx) {
      Node temp = q[parentIdx];
      q[parentIdx] = q[idx];
      q[idx] = temp;
      return heapify(parentIdx);
    }
  }
}

class Node {
  int distance;
  int vertex;

  Node(this.distance, this.vertex);
}

int mstPrim(v, e, List<List<int>> edges) {
  HashMap<int, List<List<int>>> adj = HashMap();

  for (int i = 0; i < v; i++) {
    adj[i] = [];
  }

  edges.forEach((List<int> element) {
    int s = element[0];
    int e = element[1];
    int d = element[2];
    adj[s]!.add([e, d]);
    adj[e]!.add([s, d]);
  });

  List<bool> mst = List.generate(v, (_) => false);
  List<int> distance = List.generate(v, (_) => 10000);

  int minLength = 0;
  int go = 0;
  distance[go] = 0;
  Heap heap = Heap();
  heap.push(Node(go, go));

  while (heap.q.length > 1) {
    Node start = heap.pop();

    if (mst[start.vertex]) {
      continue;
    }

    mst[start.vertex] = true;
    minLength += start.distance;

    if (adj.containsKey(start.vertex)) {
      adj[start.vertex]!.forEach((List<int> e) {
        int endNum = e[0];
        int dist = e[1];

        if (!mst[endNum] && distance[endNum] > dist) {
          distance[endNum] = dist;
          heap.push(Node(distance[endNum], endNum));
        }
      });
    }
  }

  return minLength;
}

void main() {
  List<List<int>> nodes = [
    [0, 5, 60], 
    [0, 1, 32], 
    [0, 2, 31], 
    [0, 6, 51], 
    [1, 2, 21], 
    [2, 4, 46], 
    [2, 6, 25], 
    [3, 4, 34], 
    [3, 5, 18], 
    [4, 5, 40], 
    [4, 6, 51]
  ];
  
  print(mstPrim(7, 11, nodes));
}
