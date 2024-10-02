# LeetCode

## 207. Course Schedule

### Python

#### 첫번째 풀이

BFS 기반 위상 정렬을 활용했다. 

위상 정렬을 한 후에 사이클이 있으면 course 를 마칠 수 없고 사이클 없이 탐색이 완료 됐으면 course 를 마칠 수 있다.

주의할 점은 num_courses 값이 5라고 할때 course 로 0부터 4까지 모두 주어지는게 아닐 수 있다.

<br>

### Java

#### CourseSchedule207

Python 첫번째 풀이와 동일하게 위상 정렬을 활용했다.

<br>

#### CourseSchedule207_2

교재의 풀이를 참고했고 어려운 풀이였다. DFS 재귀를 활용해서 풀이한다.

교재의 풀이 방식을 따랐으나 한가지 다르게 한 부분이 있다. 해시맵에 key, value 를 교재와 반대로 설정했다. 해시맵에 정점 정보들을 모을 때 key 를 먼저 끝내야 할 우선 순위가 높은 정점으로 설정하고, value 를 이후에 끝내야 할 정점을 넣었다.

이외의 풀이에 대한 정보는 주석으로 남겨두었다.

<br>

<참고>

https://m.blog.naver.com/ndb796/221236874984

