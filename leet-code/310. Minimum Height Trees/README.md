# LeetCode

## 330. Minimum Height Trees

최소 높이를 갖는 트리 노드를 찾는 문제다. 트리의 가운데에 있는 노드를 찾아야 한다.

처음에 생각했던 방식은 플로이드 워셜 알고리즘을 사용해서 모든 노드간의 거리를 구한 후 노드마다 다른 노드로 가는 거리가 최소인 노드를 찾는 방식을 생각했다.

그러나 플로이드 워셜 알고리즘의 시간 복잡도는 O(N^3) 이라 최대 노드 갯수가 20000개인 이번 문제에서는 적용할 수 없었다.

<br>

교재의 방식을 참고했다. 교재는 리프 노드를 제거하는 방식으로 풀이한다. 노드의 갯수가 2개 이하로 남을 때까지 리프 노드를 제거하고 남은 노드를 리턴한다.

리프 노드는 연결된 노드가 하나인지 여부로 알 수 있다. 각 노드를 키로 하고 노드마다 연결된 노드들을 값으로 하는 딕셔너리를 만들고 값의 길이가 1이면 리프 노드다.

<br>

처음에 리프 노드를 찾고서 그 다음 while 문으로 진입한다. while 문에서는 앞서 찾은 리프 노드들을 for 문을 돌면서 해당 리프 노드와 연결된 노드간의 연결을 끊는다.

연결을 끊기 위해 리프 노드의 값을 제거한다. 리프 노드라 값이 하나기 때문에 pop 으로 리스트에서 꺼낼 수 있다. pop 으로 꺼낸 노드도 리프 노드와 연결되지 않도록 값에서 리프 노드를 찾아서 제거한다.

리프 노드를 찾아서 제거한 후 곧장 해당 노드 (pop 으로 꺼낸 노드) 도 리프 노드가 됐는지 확인한다. for 문을 다 돌고나서 확인 하는게 아니라 곧장 확인하는 이유는 남은 for 문이 돌면서 리프 노드의 값이 빈 리스트가 돼서 리프 노드인 노드를 제대로 찾을 수 없는 문제가 발생한다.

그래서 while 문 이전에 리프 노드를 먼저 찾는 과정을 while 문 안으로 옮기고 싶었으나 이런 이유로 그렇게 할 방법을 찾지 못했다.

<br>

<참고>

파이썬 알고리즘 인터뷰
