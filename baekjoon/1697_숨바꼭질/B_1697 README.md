# 백준

## 1697

2021년 6월 7일 기준으로 [Python으로 가장 빠른 코드](https://www.acmicpc.net/source/18296168) 를 추가적으로 더 공부해해봐야겠다.

이분은 재귀적인 방식으로 풀이했는데 이렇게 생각을 할 수 있다는게 대단한것 같다.

<br>

내가 풀이한 방식은 N과 K가 같으면 0을 출력, N이 K보다 크면 N - K를 출력, 그 외에는 bfs로 검사해나갔다.

100001 크기의 방문 처리할 배열을 두고 현재 위치 값에서 -1, +1, *2를 수행한 값이 만약에 K의 위치와 같으면 현재 위치까지의 시간에서 1을 더한 값을 리턴했다. K의 위치와 같지 않으면 -1 or +1 or *2를 수행한 N의 값이 0보다 크거나 같고 100000보다 작거나 같으면서 아직 방문을 하지 않은 위치라면 방문 처리를 하고서 데크에 넣어줬다.

<br>

이 문제를 풀면서 주의할 점은 soobin의 값을 계산하는 반복문을 돌때 값이 누적되서 계산되지 않도록 주의해야 한다. i가 1일때는 i가 0일때 계산된 값에서 1이 더해지면 안 된다. 즉 soobin과 seconds 값을 반복문 밖에서가 아니라 반복문 안에서 매번 새로 할당해줘야 한다. B_1697_2.js의 주석 참고.