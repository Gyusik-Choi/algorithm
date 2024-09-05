# LeetCode

## [973. K Closest Points to Origin](https://leetcode.com/problems/k-closest-points-to-origin/)

가장 가까운 위치에 있는 k 개를 구하는 문제다. 전체를 정렬하지 않고 조건에 맞는 k 개만 찾으면 되기 때문에 우선순위 큐를 활용해서 풀이했다.

우선순위 큐는 힙을 이용해서 구현할 수 있다. 

힙에 유클리드 거리와 points 리스트의 인덱스를 넣는다. k번 힙에서 꺼내고 힙에 넣었던 인덱스 정보로 points 리스트에서 값을 조회하여 리스트에 넣은 후 리턴한다.

<br>

<참고>

파이썬 알고리즘 인터뷰

자바 알고리즘 인터뷰

