# 프로그래머스

## 숫자 변환하기

BFS 혹은 DP 를 활용해서 풀이할 수 있는 문제다.

DFS, BFS 중에 어떤 알고리즘을 활용해야 할지 판단하는 기준을 잘 세워야 한다는 것을 느낄 수 있는 문제였다.

<br>

### BFS 풀이

이번 문제는 경우의 수가 몇 개인지 판단하는게 아니라 최소 횟수 하나를 구하는 문제다. DFS 가 아닌 BFS 를 활용해야 한다.

시작점인 x 값을 덱에 넣고 덱이 빌 때까지 while 문을 돌면서 3가지 연산 결과에 대한 값이 y 보다 작고 중복 연산을 막기 위해 이전에 연산된 값이 아닌 경우 덱에 추가해서 연산을 이어간다. BFS 탐색이므로 x 와 y 가 같은 경우가 나오면 이 경우가 바로 최소 횟수라 현재까지의 연산 횟수를 리턴한다.

<br>

<참고>

https://www.acmicpc.net/problem/1697

https://chanhuiseok.github.io/posts/baek-14/

https://great-park.tistory.com/19

https://velog.io/@lifeisbeautiful/%EB%B0%B1%EC%A4%80-1697%EB%B2%88-%EC%88%A8%EB%B0%94%EA%BC%AD%EC%A7%88-DP-Java-Kotlin

https://studyposting.tistory.com/93

