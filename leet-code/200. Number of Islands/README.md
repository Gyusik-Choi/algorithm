# LeetCode

## 200. Number of Islands

### Python 

#### 첫번째 풀이

재귀적으로 dfs 탐색을 수행했다.

visited 배열로 방문 체크를 하고 방문하지 않은 육지에 대해서 dfs 탐색을 했다.

총 dfs 탐색 횟수를 세서 리턴한다.

dfs 를 바깥에 두지 않고 중첩 함수로 둬서 파라미터 갯수를 줄이고 보다 편하게 변수들을 참조했다.

<br>

#### 두번째 풀이

교재의 풀이를 참고했다. 

첫번째 풀이와 달리 visited 리스트와 방향 정보를 담는 리스트를 사용하지 않는다.

방문 정보를 grid 리스트에 직접 표기하기 때문에 별도로 visited 리스트를 사용할 필요가 없다.

dfs 탐색을 4번의 재귀 호출로 하면서 방향 정보를 담는 리스트를 사용할 필요가 없다.

<br>

### Java

#### NumberOfIslands200

재귀를 활용해서 풀이했다.

<br>

#### NumberOfIslands200_2

교재의 풀이를 참고했다.

NumberOfIslands200 풀이와 달리 별도의 방문 배열과 yValue, xValue 와 같은 4방향의 값을 나타내는 별도의 배열을 사용하지 않는다.

<br>

#### NumberOfIslands200_3

NumberOfIslands200 와 달리 방향 정보를 담는 리스트를 인스턴스 변수로 선언해서 사용했다.

NumberOfIslands200 와 달리 별도의 방문 배열을 사용하지 않았다.

NumberOfIslands200 와 달리 방문 처리를 dfs 함수 안에서만 했다.

<br>

### Kotlin

#### NumberOfIslands200

교재의 풀이를 참고했다.

NumberOfIslands200_2 의 풀이를 코틀린으로 변경했다.

NumberOfIslands200_2 와 달리 방문 가능한 정점인지를 판단하는 부분을 if 문이 아닌 when 구문을 적용했고, 중첩 함수를 사용해서 grid 값을 별도의 파라미터로 전달하지 않고 참조할 수 있었다.

<br>

#### NumberOfIslands200_2

NumberOfIslands200_3.java 와 동일한 방식으로 풀이했다.

그렇지만 when 구문을 사용해서 if 문을 사용하지 않고 보다 간결하게 풀이했다.

<br>

<참고>

파이썬 알고리즘 인터뷰

https://github.com/onlybooks/python-algorithm-interview/blob/master/4-non-linear-data-structures/ch12/32-1.py

자바 알고리즘 인터뷰

