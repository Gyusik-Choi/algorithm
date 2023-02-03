# 백준

## 10825

이것이 코딩테스트다에 수록된 문제로 정렬 유형의 문제다.

<br>

### Python

파이썬의 람다식을 이용해 비교적 짧은 코드로 풀이할 수 있다. 

첫번째 풀이가 두번째 풀이보다 메모리 사용량도 작았고 속도도 더 빨랐다.

<br>

### JavaScript

문자열을 정렬하려면 뺄셈으로 비교를 하면 안되고 대소 비교를 통해 -1, 1 등을 리턴하는 방식을 사용해야 한다.

문자열을 뺄셈을 해버리면 NaN 이 나오게 되므로 return 값이 정수가 될 수 없다.

```javascript
const names = ['Steve', 'Bill'];

// 오름차순
names.sort((a, b) => a > b ? 1 : -1);

// 내림차순
names.sort((a, b) => a > b ? -1 : 1);
```

<br>

정수를 정렬한다면 뺄셈으로 비교가 가능하다.

```javascript
const numbers = [2, 5, 1, 4, 3];

// 오름차순
numbers.sort((a, b) => a - b);

// 내림차순
numbers.sort((a, b) => b - a);
```

<br>

<참고>

https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Array/sort

https://tesseractjh.tistory.com/53