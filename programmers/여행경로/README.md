# 프로그래머스

## 여행경로

### Python

어려운 문제였다.

그래프 탐색 유형의 문제로 DFS 재귀를 활용해서 풀이했다.

모든 여행지를 방문할 수 있는 티켓이 주어지는데 알파벳 순서대로 방문한다고 해서 무조건 모든 여행지를 방문할 수 있는게 아니다. ICN 을 시작으로 ICN 에서 갈 수 있는 도시로, 해당 도시에서 또 다시 이어진 도시로 방문을 이어가야 한다.

방문할 도시가 남았는데도 이어진 경로가 없어서 다음 도시로 넘어가는 경우가 있을 수 있어서 이런 경우는 해당 방문을 취소하고 돌아와서 다음 알파벳 순서의 도시를 먼저 방문해야 한다.

예를 들어 tickets이 [['ICN', 'BOO'], ['ICN', 'COO'], ['COO', 'DOO'], ['DOO', 'COO'], ['BOO', 'DOO'], ['DOO', 'BOO'], ['BOO', 'ICN'], ['COO', 'BOO']] 라고 가정한다. 

'ICN', 'BOO', 'DOO', 'BOO', 'ICN', 'COO' 까지 왔을 때 'COO' 에서 'BOO' 로 가면 'BOO' 에서 더 이상 갈 수 있는 도시가 없지만 'DOO' 에서 'COO' 로 가는 루트가 남는다. 루트가 계속 이어지려면 'COO' 에서 'BOO' 가 아닌 'DOO' 로 가야 모든 방문 가능한 도시를 끊기지 않고 이어서 방문할 수 있다.

<br>

문제에 명시되진 않았지만 중복 티켓이 있을 수 있다.

예를 들어 tickets 이 [["ICN", "AAA"], ["ICN", "AAA"], ["ICN", "AAA"], ["AAA", "ICN"], ["AAA", "ICN"]] 라고 가정한다.

기존에 방문 처리를 이중 딕셔너리를 사용했지만 딕셔너리는 키 중복이 되지 않는다. 딕셔너리를 사용은 하되 이중 딕셔너리가 아니라 값은 리스트로 했다. 

ICN 에서 AAA 를 3번 갈 수 있다. 앞에서 언급한 이중 딕셔너리로 할 경우 AAA 는 1개로 처리된다.

```python
visit = {
    'ICN': {
        'AAA': False,
    },
}
```

<br>

AAA 3개를 모두 처리할 수 있도록 딕셔너리의 값을 딕셔너리가 아닌 리스트로 변경했다. 리스트는 인덱스를 기반으로 한다.

```python
visit = {
	'ICN': [False, False, False],    
}
```

<br>

### Java

[이 문제](https://leetcode.com/problems/reconstruct-itinerary/description/) 와 거의 동일하다.

DFS 를 활용하되 방문 정보를 리스트 대신 다른 방식을 사용했다. 별도의 방문 정보를 담는 자료구조를 사용하지 않고, 여행 경로를 담는 자료구조만으로 풀이했다. 여행 경로를 담는 해시맵을 사용하고 해시맵의 value 를 우선순위 큐를 사용했다. 우선순위 큐를 통해 별도의 오름차순 정렬 없이 풀이할 수 있고, 목적지는 우선순위 큐에서 하나씩 제거하면서 자연스럽게 방문한 목적지는 우선순위 큐에서 제거된다.

<br>

### Kotlin

Java 풀이와 동일한 방식으로 풀이했다.

<br>

<참고>

https://school.programmers.co.kr/questions/10332

https://school.programmers.co.kr/questions/33058

https://ljhyunstory.tistory.com/107

https://ckd2806.tistory.com/entry/%ED%8C%8C%EC%9D%B4%EC%8D%AC-python%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EC%97%AC%ED%96%89%EA%B2%BD%EB%A1%9C-%EC%BD%94%EB%93%9C-%ED%92%80%EC%9D%B4-%EB%81%84%EC%A0%81%EB%81%84%EC%A0%81

파이썬 알고리즘 인터뷰

자바 알고리즘 인터뷰

