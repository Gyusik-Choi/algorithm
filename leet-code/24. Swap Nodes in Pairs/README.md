# LeetCode

## 24. Swap Nodes in Pairs

### Python

#### 24_swap_nodes_in_pairs.py

노드를 뒤집는 방법만 고민을 했는데 값만 뒤집어도 된다는 것을 전혀 생각하지 못했다.

<br>

#### 24_swap_nodes_in_pairs_2.py

교재의 풀이법을 참고했다.

선언 부분의 next 와 대입 부분의 next 를 잘 구분하는게 중요하다. 선언 부분의 next 는 해당 노드의 속성이라면 대입 부분의 next 는 노드 자체다.

<br>

### Java

#### SwapNodesInPairs24

재귀로 풀이했다. 두 칸씩 이동하는 노드를 이동하면서 연결리스트가 null (연결리스트 길이가 짝수) 이거나 연결리스트가 하나(연결리스트 길이가 홀수)만 있을 때 해당 연결리스트를 리턴한다.

리턴받은 결과를 연결리스트의 현재 노드와 다음 노드를 뒤집은 후 연결한다. 그리고 이 노드를 다시 리턴하는 방식으로 전개한다.

<br>

#### SwapNodesInPairs24_2

교재의 풀이를 참고했다. 반복 구조로 풀이한다.

두 노드를 뒤집을 때 이전 노드와의 연결은 어떻게 변경해야 할지 방법이 잘 떠오르지 않았는데 교재의 풀이를 통해 해결할 수 있었다.

<br>

````
// 입력
1 -> 2 -> 3 -> 4

// 임시 노드를 head 앞에 생성하고
// 생성한 임시 노드를 기준점인 변수 node 의 시작점으로 설정한다
0 -> 1 -> 2 -> 3 -> 4
````

뒤집을 노드의 한 칸 앞을 기준으로 접근하는게 핵심이다.

뒤집을 대상을 묶으면 (1, 2), (3, 4) 인데 기준점인 변수 node 를 뒤집을 대상보다 한 칸 앞인 0, 2에 두는 방식으로 풀이한다.

<br>

기준점인 node 변수가 0에 있을 때, 1을 3과 연결하고 0을 2와 연결한 후 2를 1과 연결한다. 그리고 node 는 0에서 2로 이동한다.

node 변수가 2에 있을 때는 3과 null(4의 next 는 null) 2와 4를 연결한 후 4와 3을 연결한다. 그리고 node 는 null 이 되면서 while 문이 종료된다.

<br>

#### SwapNodesInPairs24_3

SwapNodesInPairs24_2 와 거의 동일한 방식으로 풀이한다.

<br>

### Kotlin

#### SwapNodesInPairs24

재귀를 활용해서 풀이했다.

교재의 경우 재귀 호출을 한 이후에 기존의 head 앞 노드가 head 를 바라보도록 했다면, 이 풀이는 먼저 head 와 head 앞 노드를 뒤집은 이후 재귀 호출을 했다.

<br>

<참고>

파이썬 알고리즘 인터뷰

자바 알고리즘 인터뷰

