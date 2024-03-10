# 프로그래머스

## 두 수의 나눗셈

num1, num2 는 1에서 100까지의 정수다. int 함수와 math 모듈의 floor 함수를 이용해서 풀이할 수 있다.

단, 나눗셈의 결과가 음수면 int 와 math.floor 의 연산 결과가 다를 수 있다.

```python
print(int(-7 / 3 * 1000))
# -2333
```

<br>

```python
import math


print(math.floor(-7, 3 * 1000))
# -2334
```

