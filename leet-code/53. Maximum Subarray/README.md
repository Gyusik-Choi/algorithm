# LeetCode

## [53. Maximum Subarray](https://leetcode.com/problems/maximum-subarray/)

다이나믹 프로그래밍 유형의 문제다. 백준에도 유사한 [문제](https://www.acmicpc.net/problem/1912)가 있다.

교재의 풀이를 참고해서 별도의 dp 배열을 사용하지 않고 풀이할 수 있었다. nums 에 바로 더하는 방식을 통해 공간 복잡도를 줄였다. 

nums 를 인덱스 1부터 for 문을 돌면서 현재 인덱스의 값에서 직전 인덱스 값을 더했을 때 현재 인덱스의 값보다 크면 더하고, 현재 인덱스의 값보다 작으면 더하지 않고 현재 인덱스 값을 유지한다. 현재 인덱스 값을 유지하는 것은 기존까지의 누적합을 끊고 현재 인덱스부터 다시 누적합을 구하는게 된다.

nums 에 직접 더하기 때문에 nums 의 각 인덱스는 각 인덱스까지의 최대 누적합을 갖게 된다. for 문을 마친 후 nums 에서 최대값을 구하면 최대 부분 누적합을 구할 수 있다.

<br>

<참고>

파이썬 알고리즘 인터뷰

https://www.acmicpc.net/problem/1912

