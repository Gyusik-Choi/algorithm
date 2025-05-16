# LeetCode

## 543. Diameter of Binary Tree

### Python

어려운 문제였다.

한 정점에서 다른 정점으로 가는 최대 거리를 구하는데 루트를 통해서 가야만 하는게 아니다. 정점 간의 최대 거리를 구하는 문제다.

자식 노드의 값에서 2를 더하면 현재 노드의 트리 구조에서 가장 긴 정점 간의 거리가 된다.

```python
longest = max(longest, left + right + 2)
```

<br>

자식 노드 값은 해당 노드의 자식 노드 간의 최대 값에 1을 더한 값이다. 

```python
return max(left, right) + 1
# max(-1, -1) + 1 = 0
```

<br>

한 자식 노드가 자신의 자식 노드가 하나도 없을 경우 이 노드의 값은 0이 된다. 재귀 호출을 통해 맨 마지막 노드까지 내려가고 맨 마지막 노드는 자식 노드가 없기 때문에 한번 더 재귀호출이 발생하면 None 이 인자로 들어가고 -1을 반환한다.  

```python
def dfs(vertex):
    if not vertex:
        return -1
    
    left = dfs(vertex.left)
    right = dfs(vertex.right)
    # ...
```

<br>

### Java

#### DiameterOfBinaryTree543

재귀를 활용했다. 

재귀로 리턴하는 값이 정답이 아니라 재귀로 리턴하는 값을 바탕으로 정답을 따로 구해야 해서 별도의 static 변수를 사용했다. 이 변수의 값은 공유되기 때문에 함수를 여러번 호출하더라도 직전 함수 호출의 영향이 없도록 하기 위해 정답을 리턴하기 전에 정답은 별도의 변수로 저장하고 static 변수를 초기화 한다.

노드의 깊이를 구하는게 아니라 깊이를 바탕으로 노드의 최대 직경을 구해야 한다. 재귀호출로는 깊이를 구하고 구한 깊이들을 더해서 직경을 구해야 한다.

노드가 null 이면 0을 리턴하도록 한다. 노드가 null 이 아니면 노드의 왼쪽, 오른쪽 자식 노드를 재귀호출 한다. 현재 노드까지의 최대 직경은 기존에 구한 최대 직경 혹은 왼쪽 자식노드의 리턴값과 오른쪽 자식 노드의 리턴값의 합에 1을 더한 값 중 하나다. 현재 정점의 최대 깊이는 왼쪽 자식노드의 리턴 값과 오른쪽 자식 노드의 리턴값 중 더 큰 값에 1을 더한 값이다.

그런데 한가지 유의할 점은 최대 직경은 정점의 갯수가 아닌 간선의 갯수로 구해야 해서 위의 방식으로 구한 최대 직경에서 1을 빼야 한다.

<br>

### Kotlin

#### DiameterOfBinaryTree543

풀이방법은 DiameterOfBinaryTree543 와 동일하다. 언어를 Java 에서 Kotlin 으로 변경하면서 Kotlin 의 중첩 함수를 통해 보다 간결하게 풀이할 수 있었다.

DiameterOfBinaryTree543 와 달리 정답을 구하는 변수를 함수 밖에 두지 않고 함수 내부에 두고 재귀 함수를 중첩 함수로 해서 diameterOfBinaryTree 함수 안에서 정답을 구할 수 있었다.

<br>

<참고>

https://leetcode.com/problems/diameter-of-binary-tree/description/comments/1566534

https://leetcode.com/problems/diameter-of-binary-tree/description/comments/1575874

파이썬 알고리즘 인터뷰

자바 알고리즘 인터뷰

