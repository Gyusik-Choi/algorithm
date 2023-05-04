# 프로그래머스

## 명예의 전당 (1)

### 명예의 전당 (1).py

score 리스트를 for loop 돌면서 score 의 원소를 hall_of_fame 에 넣고 내림차순 정렬한다. hall_of_fame 리스트의 길이가 k 보다 크다면 마지막 원소를 제거한다. k 보다 크지 않다면 마지막 원소를 제거하지 않는다. 그리고 hall_of_fame 의 마지막 원소를 lowest_points_from_hall_of_fame 에 담는다.

score 리스트의 for loop 를 모두 돌고난 후 lowest_points_from_hall_of_fame 를 리턴한다.

<br>

### 명예의 전당 (1)_2.py

heapq 모듈을 활용했다. 완전히 정렬될 필요 없이 최소 값만 구할 수 있으면 된다.

score 리스트를 for loop 돌면서 heapq 의 heappush 메소드를 통해 hall_of_fame 에 score 의 원소를 넣는다. 원소를 넣고나면 heapq 에서 알아서 최소값을 hall_of_fame 의 맨 첫번째 인덱스에 둔다. 명예의 전당 (1)_2.py 의 풀이와 달리 sort 코드를 명시적으로 작성할 필요가 없어진다.

hall_of_fame 의 길이가 k 보다 크다면 heapq.heappop 메소드를 통해 hall_of_fame 리스트에서 값을 제거한다.  k 보다 크지 않다면 값을 제거하지 않는다. 그리고 그리고 hall_of_fame 의 마지막 원소를 lowest_points_from_hall_of_fame 에 담는다.

score 리스트의 for loop 를 모두 돌고난 후 lowest_points_from_hall_of_fame 를 리턴한다.

