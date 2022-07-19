import 'dart:collection';

bool isCycle(List<int> level) {
  for (int i = 1; i < level.length; i++) {
    if (level[i] == 0) {
      return false;
    }
  }

  return true;
}

List<int> bfs(List<List<int>> matrix, List<int> level, Queue<int> q) {
  List<int> answer = [];

  while (q.isNotEmpty) {
    int popedNode = q.removeFirst();
    answer.add(popedNode);

    for (int i = 0; i < matrix[popedNode].length; i++) {
      level[matrix[popedNode][i]] -= 1;

      if (level[matrix[popedNode][i]] == 0) {
        q.add(matrix[popedNode][i]);
      }
    }
  }

  if (isCycle(level)) {
    return [-1];
  }

  return answer;
}

Queue<int> findZeroLevel(List<int> level) {
  Queue<int> q = Queue<int>();

  for (int i = 1; i < level.length; i++) {
    if (level[i] == 0) {
      q.add(i);
    }
  }

  return q;
}

List<int> topologySort(List<List<int>> arr) {
  List<List<int>> matrix = [];
  List<int> level = [];

  int node_num = arr[0][0];
  int node_info_length = arr[0][1];

  for (int i = 0; i <= node_num; i++) {
    matrix.add([]);
    level.add(0);
  }

  for (int i = 1; i <= node_info_length; i++) {
    int start_node = arr[i][0];
    int end_node = arr[i][1];

    matrix[start_node].add(end_node);
    level[end_node] += 1;
  }

  Queue<int> q = findZeroLevel(level);
  List<int> answer = bfs(matrix, level, q);
  return answer;
}

void main() {
  List<List<int>> arr = [[7, 8], [1, 2], [1, 5], [2, 3], [2, 6], [3, 4], [4, 7], [5, 6], [6, 4]];
  print(topologySort(arr));
}

// 7 8 (정점 수, 간선 수)
// 1 2
// 1 5
// 2 3
// 2 6
// 3 4
// 4 7
// 5 6
// 6 4
// => 1 2 5 3 6 4 7

// 참고
// https://api.flutter.dev/flutter/dart-collection/Queue-class.html
