# LeetCode

## 200. Number of Islands

### 첫번째 풀이

재귀적으로 dfs 탐색을 수행했다.

visited 배열로 방문 체크를 하고 방문하지 않은 육지에 대해서 dfs 탐색을 했다.

총 dfs 탐색 횟수를 세서 리턴한다.

dfs 를 바깥에 두지 않고 중첩 함수로 둬서 파라미터 갯수를 줄이고 보다 편하게 변수들을 참조했다.

<br>

### 두번째 풀이

교재의 풀이를 참고했다. 

첫번째 풀이와 달리 visited 리스트와 방향 정보를 담는 리스트를 사용하지 않는다.

방문 정보를 grid 리스트에 직접 표기하기 때문에 별도로 visited 리스트를 사용할 필요가 없다.

dfs 탐색을 4번의 재귀 호출로 하면서 방향 정보를 담는 리스트를 사용할 필요가 없다.



<br>

<참고>

파이썬 알고리즘 인터뷰

https://github.com/onlybooks/python-algorithm-interview/blob/master/4-non-linear-data-structures/ch12/32-1.py

