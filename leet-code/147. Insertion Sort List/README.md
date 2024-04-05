# LeetCode

## [147. Insertion Sort List](https://leetcode.com/problems/insertion-sort-list/)

어려운 문제였다. 교재의 풀이를 이해하는 것도 쉽지 않았다.

연결 리스트를 삽입 정렬로 정렬해야 한다.

이중 연결 리스트가 아닌 단일 연결 리스트라 루트 방향으로 탐색을 할 수 없어서 어떻게 구현할 수 있을지 궁금했다. 결론적으로 교재의 풀이는 루트가 있는 왼쪽으로 탐색하지 않고 루트 방향에서 오른쪽으로 탐색을 한다.

<br>

### 첫번째 풀이

head 노드와 별도로 cur, parent 노드를 생성한다. 

cur 노드는 val 을 None 으로 설정한 루트 노드를 계속 바라보면서 next 를 갱신한다. 루트 노드를 바라보면서 하위 노드를 갱신한다.

head 를 처음부터 끝까지 while 문으로 순회하면서 내부적으로 head 보다 큰 cur 가 나올 때까지 또 다른 while 문을 순회한다. cur 보다 크면서 cur.next 보다 작은 head 를 찾아서 cur 과 cur.next 사이에 놓는다. 탐색을 이어나갈 수 있게 head 는 head.next 로 이동하면서 앞으로 나아간다. 

그리고 cur 에 루트 노드를 보고 있는 또 다른 노드인 parent 를 할당하면서 다시 cur 를 루트 노드부터 탐색할 수 있도록 한다. 

while 문을 돌면서 계속해서 루트 노드부터 탐색한다.

<br>

### 두번째 풀이

첫번째 풀이에서는 cur 를 매번 루트 노드로 이동 시킨다. head 가 cur 보다 크서 cur.next 보다 작은 위치를 찾아야 하는데 cur 보다 head 가 이미 큰 경우는 다시 루트 노드로 이동할 필요가 없이 현재 위치에서 탐색을 해도 된다.

두번째 풀이에서는 이런 불필요한 루트 노드로 이동하는 부분을 제거하고 필요한 경우만 cur 가 루트 노드로 돌아가도록 개선했다.

<br>

<참고>

파이썬 알고리즘 인터뷰
