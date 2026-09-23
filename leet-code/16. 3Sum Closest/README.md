# LeetCode

## [16. 3Sum Closest](https://leetcode.com/problems/3sum-closest/)

자바 알고리즘 인터뷰 교재에 있는 [LeetCode - 3Sum](https://leetcode.com/problems/3sum/description/) 와 유사한 문제다.

### Java

정렬과 투 포인터를 활용했다.

배열을 정렬하면 투 포인터로 세 요소의 합(이하 sum)과 target 의 차이를 줄일 수 있다. sum 이 target 보다 작으면 sum 을 증가 시키기 위해 왼쪽 포인터를 늘리고, sum 이 target 보다 크면 sum 을 감소 시키기 위해 오른쪽 포인터를 줄인다.

target 과 기존의 가장 가까운 값(이하 closest)의 차이보다 target 과 sum 의 차이가 더 작으면 closest 를 갱신한다.

<br>

<참고>

자바 알고리즘 인터뷰

