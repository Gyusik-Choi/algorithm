# 백준

## 5014

BFS 를 이용해서 풀이할 수 있다.

모든 경우의 수를 구하는게 아니라 최단 횟수를 구해야 하므로 DFS 보다 BFS 가 적절하다.

S 를 출발점으로 해서 덱에 넣고 덱이 빌 때까지 while 문을 돈다. while 문 안에서 for 문을 2번 돌면서 한번은 U 버튼을 누르고 다른 한번은 D 버튼을 누른다.

건물이 F층까지 있어서 F층 보다 높은 층으로 갈 수 없고, 건물은 1층부터 시작이라 1층 보다 아래 층으로 갈 수 없다. U 버튼을 눌렀을 때 F 층 보다 높으면 덱에 포함하지 않는다. D 버튼을 눌렀을 때 1층 보다 낮은 경우도 덱에 포함하지 않는다.

덱에 넣을 때 한가지 더 고려할게 있다. 중복 검사를 막기 위해 해당 층을 갔었는지 확인하는 visited 배열을 사용한다. visited 배열에서 해당 층의 인덱스가 True 면 덱에 넣지 않는다.

U 혹은 D 버튼을 눌러서 G 층이라면 지금까지 버튼을 누른 횟수에 1을 더해서 리턴한다.