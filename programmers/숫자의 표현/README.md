# 프로그래머스

## 숫자의 표현

완전 탐색으로 풀이했다. 

1부터 n 까지 for 문을 돌면서 각 요소부터 1씩 더한 숫자의 누적합이 n과 같으면 갯수를 세는 변수 sums 에 1을 더해줬다.

연속한 자연수들을 구해야하고 각 자연수마다 자신으로 시작하는 경우의 수는 최대 1개씩만 가능하다. 그래서 1부터 n까지 각 자연수로 시작하는 연속한 자연수의 합이 n과 같은 경우를 찾으려 했다.

