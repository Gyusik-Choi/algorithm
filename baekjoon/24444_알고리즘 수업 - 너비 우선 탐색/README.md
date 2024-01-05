# 백준

## 24444

[24479](https://www.acmicpc.net/problem/24479), [24480](https://www.acmicpc.net/problem/24480) 문제와 유사하며 DFS 대신 BFS 로 탐색하는게 다르다.

BFS 로 탐색하기 위해 큐를 이용한다.

<br>

출력을 한번만 하려다 하나씩 출력하는 방식으로 바꿨다.

```python
answer = ''
for i in range(1, N + 1):
    answer += str(visit[i]) + "\n"
sys.stdout.write(answer)
```

<br>

위의 코드보다 아래의 코드가 제출시 약 5배 정도 빨랐다. 나머지 코드는 모두 동일했다.

```python
for i in range(1, N + 1):
    sys.stdout.write(str(visit[i]) + "\n")
```

