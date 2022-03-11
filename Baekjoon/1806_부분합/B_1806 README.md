# 백준

## 1806

### B_1806.py

투포인터 중에서도 슬라이딩 윈도우 유형의 문제다. [백준 3273번](https://www.acmicpc.net/problem/3273), [백준 2740번](https://www.acmicpc.net/problem/2470)과 달리 정렬하지 않으며 양끝에 포인터를 두는게 아니라 시작점에 두 포인터를 두고 출발한다.

두 포인터 start, end를 0으로 설정하고, 최소 길이를 구하는 min_length 값을 N으로 하며 수열 0번 인덱스의 값을 sums로 설정한다.

while문을 start가 end보다 작거나 같으면서 end가 수열의 길이인 N보다 작을때 까지 반복한다.

sums가 부분합 S보다 작으면 sums가 더 커져야 한다. end 값을 1 늘려주고 늘린 인덱스의 값을 sums에 더해준다.

sums가 부분합 S보다 크면 sums가 더 작아지도록 해야한다. 현재 start 인덱스의 값을 sums에서 빼주고, end와 start 사이의 거리(end - start + 1)을 min_length와 비교해서 더 작으면 값을 갱신해준다. 그리고 start 값을 1 늘려준다.

이렇게 해서 구해진 min_length가 정답이 된다.

<참고>

파이썬 알고리즘 인터뷰(저자: 박상길)

https://rightbellboy.tistory.com/82

