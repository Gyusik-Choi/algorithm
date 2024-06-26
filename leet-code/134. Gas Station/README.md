# LeetCode

## [134. Gas Station](https://leetcode.com/problems/gas-station/)

그리디 유형의 문제로 교재의 풀이를 참고했다.

문제의 조건으로 정답을 찾을 수 있는 경우가 한개임이 보장된다. 요건을 충족하면 반드시 정답이 단 하나가 존재한다. 요건은 gas 의 총합이 cost 의 총합 보다 크거나 같아야 한다. 

gas 의 총합이 cost 의 총합 보다 작으면 어느 지점에서 출발하건 cost 가 더 큰 지점이 발생하므로 정답을 구할 수 없다. 반면에 gas 의 총합이 cost 의 총합 보다 크거나 같으면 (정답이 한개인 문제의 조건에 따라) 정답을 구할 수 있는 유일한 지점을 찾을 수 있다.

gas 의 총합과 cost 의 총합을 비교해서 cost 의 총합이 더 큰 경우가 아니라면 정답을 반드시 찾을 수 있다.

탐색하는 동안 gas 의 합이 cost 의 합 보다 작은 경우가 발생하면 해당 정점까지는 정답이 될 수 없다. 최초 정점부터 현재 정점까지 방문 했을 때 결국 cost 가 더 크기 때문에 최초 정점과 현재 정점 사이에서 어느 정점에서 출발하든 결국 현재 정점까지의 gas  합이 cost  합보다 큰 경우가 나올 수 없다.

유일한 한 정점이 정답으로 보장 되므로 현재 정점 이후의 정점이 정답 가능한 후보가 될 수 있다.

<br>

<참고>

파이썬 알고리즘 인터뷰

