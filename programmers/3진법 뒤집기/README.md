# 프로그래머스

## 3진법 뒤집기

10진수를 3진수로 변환하기 위해 while 문을 돌면서 n 이 1이상인 경우에 n 을 3으로 나눈 나머지 값을 문자열로 변환해서 변수에 더하고 n 은 3으로 나눠준다. 순차적으로 변수에 더하면 3진수를 따로 뒤집을 필요 없이 문제에서 요구하는 뒤집은 3진수를 구할 수 있다.

<br>

3진수를 10진수로 직접 변경할 수 있고 아니면 int 함수를 사용할 수도 있다.

풀이에서는 직접 변경하는 방법을 사용했으나 int 함수를 사용한다면 3진수를 10진수로 변경할 때 아래와 같은 방법으로 가능하다.

```python
num = '120'
int(num, 3)
```

<br>

<참고>

https://docs.python.org/ko/3/library/functions.html#int

