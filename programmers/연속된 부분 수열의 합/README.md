# 프로그래머스

## 연속된 부분 수열의 합

큐를 활용해서 풀이했다. sequence 의 최대 길이가 백만이라 2차 for 문을 돌면 안 된다.

sequence 리스트를 for 문을 돌면서 요소를 sums 변수에 더한다. 

만약에 sums 가 k 보다 크다면 sums 가 k 보다 같거나 작아질 때까지 while 문을 돌면서 큐에서 요소를 제거한다. 큐에서 하나만 제거하면 안 된다.

만약에 sums 가 k 와 같고 수열의 길이가 min_length 보다 작다면 min_length 를 갱신하고 큐의 첫번째 요소와 마지막 요소를 각각 answer 의 첫번째, 두번째 인덱스 값으로 갱신한다.



