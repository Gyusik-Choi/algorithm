# LeetCode

## 347. Top K Frequent Elements

### Python

Counter 클래스와 heapq 모듈을 활용했다.

Counter 클래스로 리스트의 요소별 갯수를 세고 heapq 모듈을 통해 우선순위 큐로 요소별 갯수가 큰 순서대로 k 개 만큼 찾을 수 있다.

<br>

### Java

#### TopKFrequentElements347

정렬을 활용해서 풀이했다. 정렬을 하려면 모든 요소를 확인해야해서 정답을 구하는데 불필요한 요소들까지 정렬하게 될 수 있다.

<br>

#### TopKFrequentElements347_2

우선순위 큐를 활용해서 풀이했다. TopKFrequentElements347 와 달리 k 의 갯수만큼만 우선순위 큐에서 꺼내면 되기 때문에 나머지 요소들은 무시하면 된다.

<br>

#### TopKFrequentElements347_3

교재의 풀이를 참고했다. 정렬이나 우선순위 큐를 쓰지 않고 for 문을 돌면서 O(N) 으로 풀이한다. 보다 자세한 내용은 코드에 주석으로 작성했다.

<br>

<참고>

파이썬 알고리즘 인터뷰

자바 알고리즘 인터뷰

