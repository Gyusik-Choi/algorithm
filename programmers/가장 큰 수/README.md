# 프로그래머스

## 가장 큰 수

정렬 유형의 문제다.

단순히 문자열 정렬로는 해결할 수 없다. 예를 들어 30, 3 이 있을때 문자열로 변환해서 정렬하면 30 이 더 크다.

```python
print('30' > '3')
# True
```

<br>

이 문제에서는 30보다 3이 더 커야 한다. 그리고 34와 3 중에서는 34가 더 커야 한다. 

30과 3을 합칠 때 30을 앞에 두면 303이 되고 3을 앞에 두면 330이 된다. 330이 더 크다.

34과 3을 합칠 때 34를 앞에 두면 343이 되고 3을 앞에 두면 334이 된다. 343이 더 크다.

<br>

이렇게 두 숫자의 우선 순위를 바꿔서 합쳐본 후 더 큰 숫자를 기준으로 정렬할 수 있다. 다른 언어(ex> 자바스크립트)에서는 이 방법을 사용할 수 있는데 파이썬에서는 그러기가 어렵다.

```javascript
// JavaScript
const sorting = (a, b) => {
  const aStr = a.toString();
  const bStr = b.toString();
  return (bStr + aStr) - (aStr + bStr)
}
```

<br>

파이썬의 sort 와 sorted 함수는 key 속성으로 정렬 기준을 설정할 수 있는데 이는 값 1개로만 설정할 수 있다. 위처럼 값이 2개가 필요한 경우를 설정하기 어렵다.

```python
arr = [1, 2, 3]
sorted(arr, key=lambda x: x * 2)
```

<br>

다른 분들의 풀이를 보면 정수를 문자열로 변환한 값에 3을 곱해서 정렬을 한다. 숫자의 최대 길이가 1000이라 1의 자리 숫자를 문자열로 변환해서 3을 곱하면 길이 4로 만들 수 있다.

이 방법과 함께 추가로 풀이한 방식은 병합 정렬을 구현하면서 대소 비교 조건으로 위에서 언급한 두 숫자의 우선 순위를 바꿔서 합친 후 더 큰 숫자가 뭔지 찾는 방식이다.

<br>

모자란 자릿 수 만큼 '9' 를 채워넣는 방식도 생각했으나 이는 안 된다. 예를 들어 3이 있고 34가 있을 때 4자리수에 맞춰서 9를 채우면 3은 3999가 되고 34는 3499가 돼서 3이 34보다 더 큰 경우가 되기 때문에 안 된다.

<br>

<참고>

https://velog.io/@hyorimm/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EA%B0%80%EC%9E%A5-%ED%81%B0-%EC%88%98-in-JavaScript

https://jokerldg.github.io/algorithm/2021/05/06/most-big-number.html

https://school.programmers.co.kr/questions/57427

https://school.programmers.co.kr/questions/51327

