어려운 문제였다. DP 를 활용해서 풀이했다. 처음에 완전 탐색으로 접근 했으나 시간 초과가 발생했다.

<br>

| (i - 1, j - 1) | (i - 1, j) |
| -------------- | ---------- |
| **(i, j - 1)** | **(i, j)** |

(i, j) 값을 나머지 3 칸의 값 중 최소값 + 1로 갱신한다.

<br>

| 0     | 1    |
| ----- | ---- |
| **1** |      |

최소값인 0에서 1을 더한 1이 빈칸에 들어간다. 0이 있기 때문에 주어진 칸에서 최대 정사각형 크기는 본인 자신인 1이다.

<br>

| 1     | 1    |
| ----- | ---- |
| **1** |      |

이 경우 최소값 1에 1을 더한 2가 빈칸에 들어간다. 각자 본인 자신인 1을 값으로 갖고 있었고 빈칸 지점에서 정사각형 크기를 2로 만들 수 있다.

<br>

| 0     | 1     | 1     |
| ----- | ----- | ----- |
| **1** | **1** | **2** |

위 2개의 표를 연결해서 살펴보면 왼쪽의 0, 1을 제외하고 나머지 4칸으로 정사각형 최대 크기를 2로 만들 수 있다.

<br>

이렇게 갱신을 해나가는데 (i, j) 값이 0인 경우는 갱신하지 않는다.

y 축 기준으로 x 축 방향으로 2차 for 문을 돌면서 해당 인덱스 값이 0인 경우 직전 인덱스 값으로 덮으면 안 된다. 만약에 현재 인덱스 값을 0 여부에 관게 없이 무조건 갱신하면 현재 인덱스 값은 최소 1 이상이 된다. 관계된 영역의 최소값 + 1로 갱신하므로 관계된 영역의 값이 모두 0이면 최소값이 0이고 이 값에서 1을 더한 값으로 갱신하므로 현재 인덱스 값은 1이 된다. 갱신된 현재 인덱스에 의해 다음 인덱스도 영향을 받게 된다. 만약에 현재 인덱스가 갱신이 되지 않아서 0으로 있었다면 다음 인덱스 값이 1이라면 현재 인덱스가 0이라 최소값이 되고 여기에 1을 더한 1로 갱신되므로 값 1을 그대로 유지한다.

<br>

<참고>

https://soobarkbar.tistory.com/164

