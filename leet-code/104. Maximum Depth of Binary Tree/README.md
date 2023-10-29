# LeetCode

## 104. Maximum Depth of Binary Tree

트리 유형의 문제다.

<br>

### 첫번째 풀이

BFS 를 활용했다.

BFS 탐색에는 큐가 사용되는데 큐에서 꺼내는 연산을 보다 효율적으로 하기 위해 리스트가 아닌 deque 를 사용했다.

 deque 에 파라미터 root 를 초기 값으로 넣는다. while 문으로 deque 에 요소가 있을 때까지 반복하면서 deque 에서 꺼낸 노드의 left, right 노드를 deque 에 넣는다.

만약에 left, right 노드가 맨 마지막 자식 노드라면 left, right 값이 None 이라 deque 에 추가할 노드가 없다.

<br>

while 문 안에서 for 문이 있다. deque 의 길이만큼 for 문을 돌아야 deque 에서 요소가 꺼내질 때마다 cnt 값이 증가하지 않고 동일한 깊이의 노드를 하나의 cnt 값으로 확인할 수 있다.

<br>

파라미터 root 가 None 일 수 있어서 별도의 예외 처리를 했다.

<br>

### 두번째 풀이

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

<참고>

파이썬 알고리즘 인터뷰

https://devraphy.tistory.com/567

