# 백준

## 2108

### 파이썬

input으로 입력 받으면 시간초과가 발생한다.

sys.stdin.readline()으로 입력 받아서 시간초과를 해결했다.

<br>

산술평균, 중앙값, 최빈값, 범위를 각각 구해야하는 문제다

<br>

산술평균은 파이썬의 round 함수를 활용했다. round 메소드는 사사오입이라고도 부르는데, 수학 문제를 풀 때의 반올림과 조금 다르다.

2.5와 3.5를 반올림하라는 수학문제였다면 답은 3, 4 였을 것이다.

그러나 round 함수의 반올림은 다르다. 2와 4를 출력한다. 우선 소수점이 5보다 작은 수일 경우에 내림을 하는 것을 동일하나, 소수점이 5 이상인 경우에는 무조건 올림이 아니라 정수의 값이 짝수면 내림을하고 홀수면 올림을 하는게 차이다.

<br>

최빈값은 딕셔너리를 활용했다. 배열의 숫자를 for문으로 돌면서 하나씩 딕셔너리의 key로 오게 만들었고 key의 빈도수를 value로 담았다. 딕셔너리를 value를 기준으로 내림차순 정렬했다. 이렇게 되면 우선 value가 높은 순서로 정렬이 되지만 같은 value라면 key가 작은 순서로 정렬된다.

가장 맨 앞의 두 쌍의 빈도수가 같으면 둘 중에 더 큰 key 값을 리턴했고, 빈도수가 다르면 맨 앞의 key 값을 리턴했다.

주의할점은 딕셔너리 변수 자체를 바로 sorted 하게 되면 key만 남는 배열로 된다. key와 value를 모두 남겨야 한다면

```python
b = sorted(a.items())
```

이렇게 해야하고 이것도 딕셔너리 형태가 아닌 튜플 쌍으로 묶인 배열이 된다.

<br>

<br>

### 자바스크립트

자바스크립트를 풀면서 TypeError가 발생했다. 원인은 const로 input 변수를 선언한 후에 동일한 이름의 변수를 재선언했기 때문이다.

예를 들면

```javascript
const a = 1
a = 2
// TypeError: Assignment to constant variable.
```

이렇게 const 로 선언한 변수는 재선언하려고 하면 오류가 발생한다. const 사용에 주의해야겠다.

https://github.com/Gyusik-Choi/Algorithm/blob/master/WeirdJavascript/const.md