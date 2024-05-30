# LeetCode

## [406. Queue Reconstruction by Height](https://leetcode.com/problems/queue-reconstruction-by-height/)

어려운 문제였다. 

그리디 유형의 문제로 교재의 풀이를 참고했다.

그리디 방식으로 풀이할 수 있겠다는 부분까지는 접근했지만 구체적인 풀이방법은 잘 떠오르지 않았다.

<br>

조건(혹은 우선순위)에 맞춰서 people 을 정렬한 후 정렬된 people 을 순서대로 answer 에 담으면 된다. 

people 의 정렬 조건은 키는 내림차순, 자신보다 키가 큰 사람의 수는 오름차순이다.

peope 을 answer 에 담을 때 조건에 맞춰 정렬 했다면 다음 요소는 고려하지 않고 현재 요소를 기준에 맞춰서 answer 에 담으면 되기 때문에 그리디하게 풀이할 수 있다.

answer 에 people 을 담을때 people 의 요소 중 '자신보다 키가 큰 사람의 수'를 answer 에 넣을 인덱스로 사용한다. 문제에서 큐를 재구성할 수 있는 people 만 주어진다고 했기 때문에 인덱스가 벗어날 우려는 하지 않아도 된다.

people 을 키는 내림차순으로 정렬했기 때문에 자신보다 키가 큰 사람의 수가 같더라도 키가 큰 요소가 앞에 온다. 그래서 키가 큰 요소가 먼저 인덱스에 맞춰 들어간 후 키가 작은 요소가 기존의 키가 큰 요소의 인덱스에 들어오고 키가 큰 요소는 다음 인덱스로 밀려나면서 조건에 맞는 answer 가 구성될 수 있다.

<br>

교재에서는 우선순위 큐를 사용했는데 이 풀이에서는 정렬을 사용했다. people 요소가 추가되지 않아서 한번만 정렬하면 그대로 활용할 수 있으므로 우선순위 큐 대신 정렬로 풀이했다.
