# LeetCode

## [147. Insertion Sort List](https://leetcode.com/problems/insertion-sort-list/)

### Python

어려운 문제였다. 교재의 풀이를 이해하는 것도 쉽지 않았다.

연결 리스트를 삽입 정렬로 정렬해야 한다.

이중 연결 리스트가 아닌 단일 연결 리스트라 루트 방향으로 탐색을 할 수 없어서 어떻게 구현할 수 있을지 궁금했다. 결론적으로 교재의 풀이는 루트가 있는 왼쪽으로 탐색하지 않고 루트 방향에서 오른쪽으로 탐색을 한다.

<br>

#### 첫번째 풀이

head 노드와 별도로 cur, parent 노드를 생성한다. 

cur 노드는 val 을 None 으로 설정한 루트 노드를 계속 바라보면서 next 를 갱신한다. 루트 노드를 바라보면서 하위 노드를 갱신한다.

head 를 처음부터 끝까지 while 문으로 순회하면서 내부적으로 head 보다 큰 cur 가 나올 때까지 또 다른 while 문을 순회한다. cur 보다 크면서 cur.next 보다 작은 head 를 찾아서 cur 과 cur.next 사이에 놓는다. 탐색을 이어나갈 수 있게 head 는 head.next 로 이동하면서 앞으로 나아간다. 

그리고 cur 에 루트 노드를 보고 있는 또 다른 노드인 parent 를 할당하면서 다시 cur 를 루트 노드부터 탐색할 수 있도록 한다. 

while 문을 돌면서 계속해서 루트 노드부터 탐색한다.

<br>

#### 두번째 풀이

첫번째 풀이에서는 cur 를 매번 루트 노드로 이동 시킨다. head 가 cur 보다 크서 cur.next 보다 작은 위치를 찾아야 하는데 cur 보다 head 가 이미 큰 경우는 다시 루트 노드로 이동할 필요가 없이 현재 위치에서 탐색을 해도 된다.

두번째 풀이에서는 이런 불필요한 루트 노드로 이동하는 부분을 제거하고 필요한 경우만 cur 가 루트 노드로 돌아가도록 개선했다.

<br>

### Java

어려운 문제였다. 교재의 풀이를 참고했고, 교재의 풀이를 이해하기가 쉽지 않았다.

<br>

#### InsertionSortList147

정렬된 노드를 가리키는 p, 정렬 해야할 노드를 가리키는 head 로 나눠서 진행한다. 

p 는 정렬된 노드를 가리키고 있어서, p 를 처음부터 순회하면서 head 가 p 사이에 들어갈 위치를 탐색한다. 

연결이 끊어지지 않으면서 head 를 p 안에 넣기 위해, p 와 head 의 다음 노드를 바라보는 변수를 미리 설정한 후 p 의 next 로 head 를 설정하고 head 의 next 로 p 의 기존 next 를 연결한다.

그리고 head 는 다음 정렬해야 할 대상을 가리키기 위해 앞서 head 의 다음 노드를 바라보는 변수로 설정한다.

p 는 맨 앞으로 이동해서 처음부터 다시 head 가 들어갈 위치를 찾는다.

<br>

#### InsertionSortList147_2

InsertionSortList147 와 전체적인 풀이 방식은 동일한데 차이는 p 를 무조건 맨 앞으로 보내지 않는 점이다.

p 를 맨 앞으로 보내는 이유는 p 사이에 올 head 의 위치를 찾기 위해서다. 만약에 현재 위치의 p 보다 head 가 더 크다면 p 를 맨 앞으로 보낼 필요가 없다.

<br>

### Kotlin

#### InsertionSortList147

교재의 풀이를 참고했다. Java 의 InsertionSortList147 와 동일한 방식으로 풀이했다.

<br>

#### InsertionSortList147_2

교재의 풀이을 참고했다. InsertionSortList147 를 보다 효율적으로 개선한 풀이다.

InsertionSortList147 에서는 정렬을 하고 매번 p 를 맨 앞인 parent 로 이동하는데 이 풀이에서는 이를 방지했다.

p 가 head 보다 작으면 p 의 앞부분은 이미 p 보다 작은 값으로 정렬이 됐기 때문에 parent 로 이동할 필요가 없다. p 가 head 보다 큰 경우만 head 를 넣을 위치를 찾기 위해 p 를 parent 로 이동시킨다.

<br>

<참고>

파이썬 알고리즘 인터뷰

자바 알고리즘 인터뷰

