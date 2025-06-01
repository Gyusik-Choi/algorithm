# LeetCode

## [215. Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array/)

### Python

힙을 활용하는 문제다. heapq 모듈을 사용해서 풀이했다.

<br>

두번째 풀이처럼 heapify 를 활용해서 리스트 요소를 하나씩 넣지 않아도 한번에 최소힙을 구성할 수 있다. 다만 주의할 점은 리스트 요소가 추가되면 힙이 유지되지 않는다.

```python
arr = [2, 1, 3]
heapq.heapify(arr)
arr.append(0)
print(heapq.heappop(arr))
# 1
# 0 이 나오길 기대하지만 실제로는 1 이 나온다
```

<br>

heapify 외에 nlargest 를 이용해서 한줄에 풀이할 수도 있다.

<br>

### Java

#### KthLargestElementInAnArray215

자바의 내장 PriorityQueue 를 이용해서 풀이했다.

<br>

#### KthLargestElementInAnArray215_2

최대힙을 직접 구현해서 풀이했다.

<br>

### Kotlin

#### KthLargestElementInAnArray215

Kotlin 은 자체적으로 PriorityQueue 를 제공하지 않아서 Java 의 PriorityQueue 를 import 해서 사용하려 했으나 이상하게도 leetcode 에서 실행하면 컴파일 에러가 발생했다.

import 대신 java.util.PriorityQueue 와 같이 직접 코드 상에서 접근하는 방식으로 해결했다.

또한 Java 에서는 IntStream 으로 할 수 있었던 특정 횟수만큼 반복하는 작업을 Kotlin 에서는 repeat 함수로 대체할 수 있었다.

<br>

<참고>

파이썬 알고리즘 인터뷰

자바 알고리즘 인터뷰

