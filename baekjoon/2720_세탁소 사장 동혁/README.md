# 백준

## 2720

그리디 유형의 문제다. 

거스름돈 종류를 배열에 담고 for loop 를 돌면서 입력 받은 거스름돈 C를 for loop 의 원소와 나눠서 몫은 정답을 담는 answer 에 넣고 나머지는 C의 값으로 대입한다.

거스름돈 종류를 큰 수부터 배열에 담아서 큰 수부터 나눌 수 있는 만큼 최대한 나눠서 나머지를 최소로 한다.

나눌때는 python 의 내장 함수인 divmod 함수를 활용했다. 나눗셈의 몫과 나머지를 한번에 구해주는 함수다.



<br>

<참고>

https://docs.python.org/3/library/functions.html?highlight=divmod#divmod

https://calkolab.tistory.com/entry/baekjoon-python-2720

