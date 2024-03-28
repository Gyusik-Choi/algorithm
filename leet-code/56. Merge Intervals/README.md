# LeetCode

## [56. Merge Intervals](https://leetcode.com/problems/merge-intervals/)

정렬을 활용해서 풀이했다.

첫번째 풀이는 0번 인덱스 값을 시작 값인 cur 로 두고, 1번 인덱스부터 for 문을 돌면서 for 문의 요소인 next 를 cur 과 비교하는 방법을 사용한다.

cur 의 1번 인덱스 값이 next 의 0번 인덱스 값 보다 크거나 같으면 겹치는 경우다. 이때 cur 의 1번 인덱스 값과 next 의 1번 인덱스 값을 비교해서 둘 중 더 큰 값으로 cur 를 갱신한다.

cur 의 1번 인덱스 값이 next 의 0번 인덱스 값 보다 작은 경우 cur 을 answer 리스트에 넣는다.

for 문의 마지막 next 와 cur 을 비교한 후 cur 는 answer 에 들어가지 못했다. if 문에서는 cur 가 갱신되고 else 문에서는 기존의 cur 가 들어가고 기존의 cur 는 next 로 대치되면서 새로운 cur 가 된다. 결국 cur 는 answer 에 들어가지 못했다.

for 문을 마친후 cur 를 answer 에 넣어준다.

<br>

두번째 풀이는 교재의 풀이를 참고했다. 두번째 풀이가 훨씬 간결하다.

첫번째 풀이와 달리 cur 같은 변수를 사용하지 않고 for 문을 마친 후 별도로 요소를 넣지 않는다. for 문 안에서 비교와 정답이 완성된다.

정답을 담는 배열인 merged_lst 가 비었다면 for 문을 요소 item 을 우선 넣는다. 혹은 merged_lst 가 비어있지 않더라도 겹치지 않으면 현재 요소를 배열에 넣는다.

겹치는 경우 (merged_lst 가 비어있지 않고 merged_lst 의 마지막 요소의 1번 인덱스 값이 item 의 0번 인덱스 값보다 크거나 같으면 ) merged_lst 의 마지막 요소를 갱신한다.

for 문 안에서 리스트에 있는 요소를 갱신하거나 마지막 요소를 리스트에 넣는 작업이 이루어지기 때문에 첫번째 풀이와 달리 마지막 요소를 for 문 이후에 넣어줄 필요가 없다.

<br>

<참고>

파이썬 알고리즘 인터뷰

