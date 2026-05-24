# LeetCode

## [530. Minimum Absolute Difference in BST](https://leetcode.com/problems/minimum-absolute-difference-in-bst/)

### Java

#### MinimumAbsoluteDifferenceInBST530

[LeetCode - Minimum Height Trees](https://leetcode.com/problems/minimum-height-trees/description/) 와 동일한 문제다.

재귀와 중위 순회를 활용해서 풀이했다.

이진 탐색 트리가 입력으로 주어지기 때문에 오른쪽 자식 노드, 부모 노드, 왼쪽 자식 노드 순서로 탐색하면 이전에 방문한 노드가 현재 노드보다 항상 값이 크다.

이전에 방문한 노드의 값과 최소 거리 차이를 별도 변수로 두고 현재 값과 비교하면서 갱신해나갔다.

<br>

#### MinimumAbsoluteDifferenceInBST530_2

중위 순회를 활용하되 MinimumAbsoluteDifferenceInBST530 와 달리 재귀가 아닌 반복 구조로 풀이했다.

반복 구조로 중위 순회를 구현하기 위해 이중으로 while 문을 두었다. 바깥의 while 문은 스택이 비어있지 않거나 노드가 null 이 아니면 반복한다. 안쪽의 while 문은 노드가 null 이 아니면 반복한다.

안쪽의 while 문이 노드가 null 이 돼서 종료되더라도 스택에 노드가 남아있으면 바깥의 while 문이 종료되지 않아서 탐색을 이어나갈 수 있다.

중위 순회를 하기 위해 안쪽 while 문에서는 node 를 오른쪽으로 이동해가면서 스택에 노드를 추가한다. 그리고 노드가 null 이 되어 안쪽 while 문이 종료되면 스택에서 노드를 꺼내어 최소 거리 차이를 비교하고 이전 값을 현재 값으로 갱신한 뒤에 노드를 왼쪽 노드로 갱신한다.

<br>

<참고>

자바 알고리즘 인터뷰

