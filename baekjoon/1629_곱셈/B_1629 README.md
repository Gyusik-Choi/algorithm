# 백준

## 1629

분할정복 문제다. 입력 범위가 크기 때문에 문제에서 주어진 그대로 곱하고 나머지를 구하면 시간초과에 걸린다.

분할을 통해서 숫자를 줄여야 한다. 

10의 10제곱이라고 하면 10의 5제곱 * 10의 5제곱과 같다. 

10의 5제곱은 10의 4제곱 * 10과 같다. 

10의 4제곱은 10의 2제곱 * 10의 2제곱과 같다. 

10의 2제곱은 10 * 10과 같다.

<br>

```
10 ** 10
== (10 ** 5) * (10 ** 5)
== (10 ** 4) * (10) * (10 ** 5)
== (10 ** 2) * (10 ** 2) * (10) * (10 ** 5)
== (10) * (10) * (10 ** 2) * (10) * (10 ** 5)
```

<br>

위의 내용을 보면 분할을 하되 한쪽만 분할해나간다. 왜냐면 서로가 같은 값을 같기 때문에 하나만 구해서 곱해주면 된다. 즉, 10 ** 10을 분할하면 (10 ** 5) * (10 ** 5) 인데 10 ** 5 한쪽만 끝까지 분할해서 구한 값을 구해서 곱해주면 된다.

추가적으로 지수가 짝수인 경우와 홀수인 경우를 구분해야 한다. 짝수는 절반으로 나눌 수 있지만 홀수는 그렇게 할 수 없다. 10 ** 5를 보면 (10 ** 4) * (10)과 같다. 10 ** 4를 분할하고 10을 곱해주면 된다.

<br>

참고

https://st-lab.tistory.com/237