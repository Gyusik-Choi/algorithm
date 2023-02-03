# 백준

## 1644

### B_1644.py

에라토스테네스의 체를 이용하여 소수를 구한다.

구한 소수를 기준으로 슬라이딩 윈도우 알고리즘을 통해 풀이한다. Index error가 나지 않도록 유의해야 한다.

start, end 를 0으로 하고 limit은 prime_numbers의 길이로 하며 sums는 prime_numbers의 0번 인덱스 값으로 둔다.

start가 end 보다 작거나 같으며 end가 limit보다 작은 경우에 while문을 반복한다.

sums가 N과 같으면 sums에서 prime_numers의 start 인덱스 값을 빼주고 start를 1 더해준다.

sums가 N 보다 작은 경우(위의 경우를 수행하게 됐을 때도 이 경우를 만족하게 된다)에는 sums에서 end를 1더해주고 sums에 prime_numers의 end 인덱스 값을 더해준다. 이때 주의할점은 end + 1 < limit을 만족할 경우에만 수행을 해줘야 한다. 그렇지 않으면 end 인덱스가 limit과 같아져서 index error가 날 수 있다.

sums가 N 보다 큰 경우에는 sums가 N과 같을때와 마찬가지로 sums에서 prime_numers의 start 인덱스 값을 빼주고 start를 1 더해준다. 그래서 코드를 간략화 시킬 수가 있으며 sums가 N과 같을 때는 answer에 1을 더해주는 것을 수행해주면 된다. 다만 sums가 N과 같을 때는 answer에 1을 더해주는 것을 sums에서 prime_numers의 start 인덱스 값을 빼주고 start를 1 더해주는 것에 앞서서 수행해줘야 한다. 그렇지 않으면 index error가 발생할 수 있다.

추가적으로 N이 1인 경우에 주의해야 한다.

<br>

<참고>

https://wikidocs.net/21638

https://www.acmicpc.net/board/view/73979 