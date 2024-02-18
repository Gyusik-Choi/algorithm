# LeetCode

## [215. Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array/)

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

<참고>

파이썬 알고리즘 인터뷰

