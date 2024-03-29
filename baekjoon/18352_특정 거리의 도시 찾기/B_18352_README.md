# 백준

## 18352

### 첫번째 풀이

이것이 코딩테스트다 교재에 수록된 문제이며 bfs로 풀이했다.

최단거리를 넘어가는 거리부터는 구할 필요가 없어서 최단거리 이내의 지점들만 계산하고 끝내기 위해 dfs가 아닌 bfs로 풀이했다.

최단거리를 넘어가는 경우에 종료하는 조건을 첫 풀이에서 작성하지 않아서 시간 초과가 발생했고, 이 조건을 추가해서 통과할 수 있었다.

<br>

### 두번째 풀이

시간초과의 원인을 한참 후에야 찾게됐다. M 만큼 입력을 받는 부분에서 sys.stdin.realine() 이 아닌 input() 으로 받는 것을 발견하지 못하고 뒤늦게 발견하게 됐다. 이 부분을 수정하니 기존에 시간초과 받은 코드들도 통과가 됐다.

추가적으로 시간을 앞당길 수 있을만한 요인은 roads 를 딕셔너리가 아닌 배열로 받는 것과 for 문을 돌때 enumerate 를 활용하는 방법이 있다.

<br>

### 네번째 풀이

직접 구현한 MinHeap 클래스를 바탕으로 풀이했다. deque 를 사용했을 때보다 속도는 약 4배 정도 느렸고, 메모리 사용량은 약 2배 많았다.

<br>

### 다섯번째 풀이

heapq 모듈을 활용해서 풀이했다. 네번째 풀이보다는 약 10% 빨랐지만 메모리 사용량은 거의 동일했다.

<br>

<참고>

https://steadily-worked.tistory.com/646