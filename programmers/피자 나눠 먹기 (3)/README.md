# 프로그래머스

## 피자 나눠 먹기 (3)

나눗셈의 나머지를 고려하지 않고 몫만으로 답을 구하고 싶었다.

[이전 문제](https://school.programmers.co.kr/learn/courses/30/lessons/120814) 를 통해 배운 풀이 방법을 이번 문제에 적용했다.

slice 가 4면 동일한 피자 판수의 n 정보는 아래와 같다.

```
1판 -> 1 ~ 4
2판 -> 5 ~ 8
3판 -> 9 ~ 12
```

<br>

그런데 위의 n 을 그대로 slice 로 나누면 몫은 같지 않다. slice 가 4일때 1판에 해당하는 n 은 1 ~ 4 다. 이 n 을 slice 로 나누면 몫은 0, 0, 0, 1 이 된다.

```
slice -> 4

n -> 1
n / slice = 0

n -> 2
n / slice = 0

n -> 3
n / slice = 0

n -> 4
n / slice = 1
```

<br>

같은 몫이 나오도록 만들어주고 나눗셈을 하면 된다. n 을 slice 로 나눈 몫이 동일한 값을 갖는 범위는 slice - 1 이다. 즉 slice 가 4면 범위 3이내는 동일한 몫을 가질 수 있다.

n에서 slice - 1 을 더하면 동일한 판수의 n은 slice 로 나눴을 때 같은 몫을 갖는다. 동일한 판수의 n 범위에서 가장 작은 n을 slice 로 나누면 나머지 없이 나눠떨어질 수 있게 만든다. 가장 큰 n 은 다음 판수의 가장 작은 n - 1 까지 커지면서 몫은 동일하다.

```
slice -> 4

n -> 1
n += 3 
n -> 4
n / slice = 1

n -> 2
n += 3 
n -> 5
n / slice = 1

n -> 3
n += 3
n -> 6
n / slice = 1

n -> 4
n += 3
n -> 7
n / slice = 1
```





