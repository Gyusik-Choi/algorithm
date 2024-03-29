# 프로그래머스

## 연속 부분 수열 합의 개수

구현 유형의 문제다. 리스트 슬라이싱을 활용해서 풀이했다.

처음에 풀이한 방식은 시간 초과가 발생했다.

1차 for 문으로 1부터 elements 길이만큼 돌면서 수열의 길이를 1개부터 수열 전체 길이까지 하나씩 탐색하려 했다. 2차 for 문으로 elements 의 각 요소들을 출발점으로 하는 수열을 찾고자 했다. 2차 for 문 안에서는 while 문을 사용했다. 1차 for 문의 요소 (찾고자 하는 수열의 길이) 만큼 while 문을 반복하면서 elements 의 각 인덱스별 숫자의 합을 구하는 방식으로 연속 부분 수열의 합을 구했다.

<br>

이 방식은 시간 초과가 발생해서 개선을 시도한 방식도 시간 초과가 발생했다. 수열의 전체 길이만큼 합을 구하는 경우는 어느 인덱스를 기준으로 하더라도 값이 동일하기 때문에 1차 for 문을 1부터 elements 길이 - 1 만큼 반복하고 for 문이 다 종료되고 난 후에 elements 전체 합을 따로 구했다. 이 방식도 결국 3차 for 문에 가까운 시간 복잡도가 발생하기 때문에 시간 초과가 발생했다.

<br>

이를 다시 개선하기 위해 리스트 슬라이싱을 사용해서 통과할 수 있었다. 의문이 드는 부분은 하나씩 순차 탐색은 하지 않지만 리스트 슬라이싱을 위해 결국 슬라이싱 범위 만큼의 탐색을 수행해야 하는데 시간이 5배 전후로 차이가 났다는 점이다. 아직 리스트 슬라이싱이 어떻게 while 문을 도는 것보다 5배나 빠를 수 있었는지 이해하지 못했다.

<br>

'다른 사람의 풀이' 를 통해 참고한 풀이는 n^2 으로 풀이했다. 기존 방식이 탐색할 길이를 기준으로 각 위치별로 해당 길이만큼 찾았다면 이 방식은 위치를 기준으로 가능한 모든 길이의 수열을 찾았다. 이 방식의 장점은 추가적으로 루프를 돌 필요없이 2차 for 문의 인덱스에서 elements 의 길이를 나눈 나머지를 통해 인덱스를 찾을 수 있다. 그리고 누적해서 값을 더해가면서 자연스럽게 수열의 길이를 1씩 늘려나갈 수 있다.

