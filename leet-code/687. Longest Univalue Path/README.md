# LeetCode

## 687. Longest Univalue Path



재귀호출로 리턴하는 값은 left, right 중에서 더 큰 값이다. 하나의 트리 줄기를 left, right 의 값으로 가져간다. 그 과정에서 동일한 값을 갖는 가장 긴 경로를 찾기 위해 부모 노드와 자식 노드의 val 값을 비교한다.

부모 노드의 val 과 왼쪽 자식 노드의 val 이 같으면 left 의 값을 1 증가시키고, 그렇지 않으면 left 를 0으로 초기화한다. 부모 노드의 val 과 오른쪽 자식 노드의 val 이 같으면 right 의 값을 1 증가시키고, 그렇지 않으면 right 를 0으로 초기화한다.

가장 긴 경로를 구하기 위해 longest 와 left + right 중에서 더 큰 값으로 longest 를 갱신한다.

<br>

위에서 "하나의 줄기를 left, right 의 값으로 가져간다" 고 얘기했는데 이와 관련해서 교재에서는 아래와 같이 설명하고 있다. 하나의 줄기를 가져가는가는 방식인 것은 알겠는데 왜 그런건지 잘 이해가 안 됐는데 교재의 설명이 이를 이해하는데 도움이 됐다.

```
지금까지 합의 최대값을 계산해왔기 때문에 따라서 상태값도 합인 left + right 를 리턴해야 할 것 같다. 그러나 잠시 생각해보면, 현재 노드는 양쪽 자식 노드를 모두 연결할 수 있지만 현재 노드의 부모 노드에서는 지금의 양쪽 자식 노드를 동시에 연결할 수 없다. 단방향이므로 양쪽 자식 노드 중 어느 한쪽 자식만 택할 수 있으며, 이는 트리의 특징이기도 하다. 따라서 둘 중 큰 값을 상태값으로 리턴해준다. 어차피 한 군데만 방문할 수 있다면 더 큰 쪽을 방문하는 게 낫기 때문이다.
```

<br>

교재에서 말하는 상태값은 재귀 호출을 호출한 부분에서 left 혹은 right 로 받게되는 값이다. 현재 노드의 부모 노드는 현재 노드의 자식 노드 2개 중 하나만 선택할 수 있어서 left + right 를 리턴하지 않고 둘 중 더 큰 값 하나만 리턴한다.

<br>

<참고>

파이썬 알고리즘 인터뷰

