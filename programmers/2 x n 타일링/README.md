# 프로그래머스

## 2 x n 타일링

DP 유형의 문제다.

백준에서 유사한 문제([2 x n 타일링](https://www.acmicpc.net/problem/11726), [2 x n 타일링 2](https://www.acmicpc.net/problem/11727))를 풀이한 적이 있었다.

2 x 1 타일 혹은 1 x 2 타일을 이용해서 직사각형을 채울 수 있다.

2 x 1 타일의 경우 가로 길이 2만큼의 공간이 필요하고, 1 x 2 타일의 경우 가로 길이 1만큼의 공간이 필요하다.

가로 길이가 n 이라고 했을 때 2 x 1 타일을 배치하면 가로 길이 n - 2 에서 타일을 배치하고, 1 x 2 타일을 배치하면 가로 길이 n - 1 에서 타일을 배치한다. 즉 n - 2 에서 배치할 수 있는 방법과 n - 1 에서 배치할 수 있는 방법을 더한 값이 n 에서 타일을 배치할 수 있는 방법의 수가 된다.

<br>

<참고>

https://www.acmicpc.net/problem/11726

https://www.acmicpc.net/problem/11727

https://blog.naver.com/ndb796/221233586932

