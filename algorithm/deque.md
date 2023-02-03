# deque

## python

알고리즘 문제를 풀이할때 bfs 등을 구현하기 위해 deque를 많이 활용하게 되는데, 그간 알지 못했던 부분을 새롭게 알게 돼서 간단하게 정리해보려 한다.

deque 인스턴스를 생성할 때 2차원 배열을 인자로 넣어주면 2차원 배열의 1차원 배열 요소를 빼서 하나씩 deque에 넣는 것과 같은 형태로 deque의 인스턴스가 생성된다.

```python
from collections import deque


arr = [[1, 2], [2, 3], [3, 4]]
deq1 = deque(arr)

deq2 = deque()
for a in arr:
    deq2.append(a)

print(deq1)
print(deq2)
# deque([[1, 2], [2, 3], [3, 4]])
# deque([[1, 2], [2, 3], [3, 4]])
```



<br>

<참고>

[백준 18405 경쟁적 전염](https://www.acmicpc.net/problem/18405)