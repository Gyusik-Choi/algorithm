# 백준

## 2178

최단거리를 구하는 문제에서는 DFS보다 BFS가 효율적임을 배운 문제다.

처음에는 DFS 재귀 방식으로 탐색을 하려고 했는데 시간초과가 발생했다. DFS는 모든 경로를 다 탐색하는 방식이기 때문에 비효율적인 부분이 있었다.

[이 글](https://www.acmicpc.net/board/view/25832) 이 문제를 해결하는데 많은 도움이 됐다.

BFS로 코드를 수정할때 의문이었던 점이 방문처리를 하고나서 다른 후보 칸을 탐색할때 앞서 방문처리를 했던 곳을 풀어주지 않으면 어떻게 이 칸은 미로를 탐색할 수 있을까였다.

조금만 더 생각해보니 최단거리를 구하는 문제라 가장 먼저 N, M의 위치에 도착하면 그게 바로 정답이기 때문에 방문처리를 풀어줄 필요가 없었다.

