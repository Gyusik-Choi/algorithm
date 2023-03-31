# 프로그래머스

## 덧칠하기

그리디를 활용했다.

먼저 wall 배열을 n + 1 크기 만큼 False 로 초기화 했다. 그리고 section 배열을 for loop 돌면서 원소부터 원소 + m 만큼 for loop 를 돌면서 wall 배열을 True 로 바꿔줬다. 바꾸는 과정에서 인덱스 값이 n 을 넘어가면 안쪽 for loop 를 종료했다. section 배열을 도는 바깥쪽 for loop 는 True 면 continue 를 통해 다음 원소로 넘어갔다.