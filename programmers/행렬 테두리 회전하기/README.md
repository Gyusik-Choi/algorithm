# 프로그래머스

## 행렬 테두리 회전하기

구현, 시뮬레이션 유형의 문제다.

배열을 두개를 사용해서 풀이했다. 계속 값을 누적하는 배열(A)과 한번 회전을 하고 난 배열의 정보를 조회하기 위한 배열(B)을 사용했다.

4방향에 대해서 각각 for 문을 돌면서 해당 방향의 시작 값을 건너뛰고 다음 값부터 채워나간다. 다음 값을 채울 때 이전 인덱스 값을 가져오는데 이때 이전 인덱스를 B배열에서 조회한다.

한 방향 탐색이 끝나고 다음 방향을 탐색할 때 직전 방향 탐색에 의해 현재 방향의 첫번째 값이 변경 되었다. 변경되기 전의 값을 가져오기 위해 B배열에서 값을 조회한다.

<br>

초기 행렬을 만드는데 주의해야 한다. 1부터 가로방향으로 차례대로 숫자가 올라간다. 숫자를 가로축 인덱스에서 1을 더하고 세로축의 인덱스 값에서 가로축 길이를 곱한 값을 더해줘야 한다.

처음에 초기 행렬을 잘못 작성해서 오답이 나왔다. 가로축 인덱스에서 1을 더하는 부분은 맞았으나 세로축의 인덱스 값에서 가로축이 아닌 세로축 길이를 곱해서 제대로된 행렬을 구할 수 없었다.

<br>

<참고>

https://school.programmers.co.kr/questions/25770

