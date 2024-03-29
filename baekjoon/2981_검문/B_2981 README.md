# 백준

## 2981

어려운 문제다. 유클리드 알고리즘만으로는 해결할 수 없는 문제다. 

A, B, C 라는 숫자가 있다고 할 때 이들이 어떤 숫자로 나눴을 때 같은 나머지를 갖는다고 하고 나누는 숫자를 N이라고 하면

```
A = N * a + 나머지
B = N * b + 나머지
C = N * c + 나머지
```

이렇게 된다고 할 수 있다. 이를 조금 바꿔서 보게 되면

```
A - B = N(a - b)
B - c = N(b - c)
```

이렇게 볼 수 있다.

여기서 N은 A, B, C의 약수다.

주어진 문제의 해답을 구하기 위해서는 약수가 아니라 최대 공약수를 구해야 한다(정확히는 최대 공약수를 구한 후 이 값의 약수들을 구해야 한다). 최대 공약수를 구하기 위해서 입력 받은 숫자들을 뺀 값을 활용해야 한다. 인접한 입력 받은 숫자들을 빼주고 이 값들의 최대 공약수를 구해가면서 가장 큰 최대 공약수 값을 찾아야 한다.

예를 들어 숫자 A, B, C, D, E를 입력 받았다고 하면

인접한 숫자들을 빼서 [A - B, B - C, C - D, D - E] 배열을 만들고,

최대 공약수 = A - B

최대 공약수 = 최대 공약수 구하는 함수(최대 공약수, B - C)

최대 공약수 = 최대 공약수 구하는 함수(최대 공약수, C - D)

최대 공약수 = 최대 공약수 구하는 함수(최대 공약수, D - E)

이렇게 되면 A, B, C, D, E의 최대 공약수를 구할 수 있다.

정답은 최대 공약수가 아닌 최대 공약수의 약수들이다. 약수들을 구하기 위해서 최대 공약수까지 구하지 않고 최대 공약수의 제곱근까지만 반복문을 돌면서 약수를 구해주면 된다.

[참고][https://tmdrl5779.tistory.com/94]

