# 백준

## 2501

제곱근을 활용했다. 

1부터 제곱근(정수가 아닌 실수일 수 있어서 int() 연산으로 반내림한 정수로 만듬)까지 for loop 를 돌면서 N 과 나눈 나머지가 0이면 해당 숫자와 몫을 배열에 담았다. 

만약에 나머지가 0이면서 나눈 수와 몫이 같으면 나눈 수만 배열에 담았다.

그리고 배열의 길이보다 K 가 더 크면 0을 출력하고, 그렇지 않으면 배열을 정렬한 후에 배열에서 K - 1 인덱스의 수를 출력했다.