# 프로그래머스

## 게임 맵 최단거리

최단거리를 찾아야 해서 BFS 를 활용했다.

시작 거리를 1로 한 후에 목적지에 도착할 경우 기존 거리 값에서 1을 더한 후 리턴했다. 만약에 목적지에 도착하지 못할 경우 -1을 리턴했다.

BFS 로 탐색했기 때문에 목적지에 처음 도착한 경우가 가장 빠르다.

<br>

자바로 풀이했을 때 목적지 도착 여부 및 방문 체크를 큐에서 꺼냈을 때 하는게 아니라 큐에 넣기 전에 검사해야 시간 초과에 걸리지 않는다. 이렇게 하려면 출발점은 미리 방문 체크를 해둬야 한다.

<참고>

파이썬 알고리즘 인터뷰

자바 알고리즘 인터뷰

