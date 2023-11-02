# LeetCode

## 543. Diameter of Binary Tree

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

<참고>

https://leetcode.com/problems/diameter-of-binary-tree/description/comments/1566534

https://leetcode.com/problems/diameter-of-binary-tree/description/comments/1575874

