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

<참고>

https://m.blog.naver.com/ndb796/221236874984

