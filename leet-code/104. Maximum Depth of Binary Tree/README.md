# LeetCode

## 104. Maximum Depth of Binary Tree

트리 유형의 문제다.

<br>

### Python

#### 첫번째 풀이

BFS 를 활용했다.

BFS 탐색에는 큐가 사용되는데 큐에서 꺼내는 연산을 보다 효율적으로 하기 위해 리스트가 아닌 deque 를 사용했다.

 deque 에 파라미터 root 를 초기 값으로 넣는다. while 문으로 deque 에 요소가 있을 때까지 반복하면서 deque 에서 꺼낸 노드의 left, right 노드를 deque 에 넣는다.

만약에 left, right 노드가 맨 마지막 자식 노드라면 left, right 값이 None 이라 deque 에 추가할 노드가 없다.

<br>

while 문 안에서 for 문이 있다. deque 의 길이만큼 for 문을 돌아야 deque 에서 요소가 꺼내질 때마다 cnt 값이 증가하지 않고 동일한 깊이의 노드를 하나의 cnt 값으로 확인할 수 있다.

<br>

파라미터 root 가 None 일 수 있어서 별도의 예외 처리를 했다.

<br>

#### 두번째 풀이

재귀를 활용했다. 교재에서는 이 문제에 대해 재귀 풀이는 나오지 않고 구글링을 통해 보게 된 풀이를 참고했다.

<br>

```python
if root is None:
    return 0
```

위의 코드가 처음에 잘 이해가 되지 않았다.

맨 마지막 자식 노드에서 left, right 에 대해 재귀 호출을 하면 None 이 인자로 들어가서 0이 리턴된다. 

0을 리턴 받고서 1씩 증가하면서 상위 노드로 올라간다.

<br>

### Java

#### MaximumDepthOfBinaryTree104

재귀를 활용했다.

예외처리를 위해 파라미터인 root 가 null 인 경우 바로 0을 리턴한다.

깊이를 파라미터로 전달받기 위해 TreeNode 와 깊이를 파라미터로 갖는 별도의 함수에서 재귀호출을 한다. 

이 함수는 node 가 null 이면 깊이를 리턴한다. TreeNode 의 왼쪽, 오른쪽 자식 노드를 각각 재귀호출 하는데 이때 깊이를 1씩 더해서 인자로 넣는다.

재귀호출이 끝나고 전달받은 결과 값을 비교해서 둘 중 더 큰 값을 리턴한다.

<br>

#### MaximumDepthOfBinaryTree104_2

재귀를 활용했고 교재의 풀이를 참고했다.

MaximumDepthOfBinaryTree104 와 풀이는 유사하지만 보다 간결하다. 

이 풀이는 깊이를 파라미터로 전달하지 않고 하나의 함수로 풀이한다. 그리고 MaximumDepthOfBinaryTree104 에서는 루트 노드의 깊이를 0으로 했다면 이 풀이는 리프 노드의 깊이를 0으로 한다.

노드가 null 이면 0을 리턴하고, null 이 아니면 왼쪽, 오른쪽 자식노드를 재귀호출한다. 리프노드까지 내려가면 0을 리턴하고 상위 노드부터 1씩 증가된 값을 리턴한다.

<br>

<참고>

파이썬 알고리즘 인터뷰

https://devraphy.tistory.com/567

자바 알고리즘 인터뷰

