# 백준

## 2740

행렬의 곱셈을 풀이하는 문제다.

배열 곱셈 방식에 맞춘 3차원 반복문 형태로 풀이하고, 이 문제의 카테고리인 분할정복에 맞춰서 분할정복 방식으로 풀이를 해보려고 한다.

분할정복 방식은 슈트라센 알고리즘이 활용되는데, 처음 들어본 알고리즘인데다가 3차원 반복문 형태도 아직 제대로 이해한 상황이 아니다.

그래서 3차원 반복문부터 이해하고 슈트라센 알고리즘으로 넘어가려 한다.

NxM 행렬과 MxK 행렬을 곱한다고 하면 NxK크기가 된다. 그리고 이를 3차원 반복문으로 풀이하면 다음과 같이 풀이할 수 있다.

```python
# a = N * K
# b = M * K
c = [[0] * K for _ in range(N)] 
for i in range(N):
  for j in range(K):
    for k in range(M):
      c[i][j] = a[i][k] + b[k][j]
```

<br>

슈트라센 알고리즘은 곱셈을 줄이고 덧셈을 늘려서 시간 복잡도를 n ^ 3 보다 줄이는 알고리즘이다.
