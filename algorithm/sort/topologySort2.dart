import 'dart:collection';

List<int> topologySort(List<List<int>> arr) {
  int v = arr[0][0];
  int e = arr[0][1];

  List<int> level = getLevel(v);

  Map<int, List<int>> edges = getEdges(v);

  for (int i = 1; i <= e; i++) {
    int start = arr[i][0];
    int end = arr[i][1];

    level[end] += 1;
    edges[start]!.add(end);
  }

  Queue<int> q = Queue<int>();

  for (int i = 1; i <= v; i++) {
    if (level[i] == 0) {
      q.add(i);
    }
  }

  return bfs(q, edges, level);
}

List<int> getLevel(int v) {
  List<int> level = [];

  for (int i = 0; i <= v; i++) {
    level.add(0);
  }

  return level;
}

Map<int, List<int>> getEdges(int v) {
  Map<int, List<int>> edges = {};

  for (int i = 0; i <= v; i++) {
    edges[i] = [];
  }

  return edges;
}

bool isCycle(List<int> degree) {
  for (int i = 0; i < degree.length; i++) {
    if (degree[i] > 0) {
      return true;
    }
  }

  return false;
}

List<int> bfs(Queue<int> q, Map<int, List<int>> edges, List<int> level) {
  List<int> answer = [];

  while (q.isNotEmpty) {
    int start = q.removeFirst();

    answer.add(start);

    for (int i = 0; i < edges[start]!.length; i++) {
      int end = edges[start]![i];
      level[end] -= 1;

      if (level[end] == 0) {
        q.add(end);
      }
    }
  }

  if (isCycle(level)) {
    return [];
  }

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