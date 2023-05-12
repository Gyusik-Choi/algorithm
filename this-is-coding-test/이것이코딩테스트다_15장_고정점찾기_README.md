# 이것이 코딩테스트다

## 챕터 15 28번 고정점 찾기

### Python

이진탐색을 활용하는 문제다.

첫번째 풀이에서는 mid 인덱스의 배열 값이 mid 인덱스 보다 크면 mid 인덱스 보다 큰 인덱스의 배열 값이 해당 인덱스와 같을 수 없음을 간과했다. 

아래의 예시를 보면 2번 인덱스의 값이 7이다. 이때 3, 4번 인덱스의 배열 값은 자신의 인덱스와 같은 값이 될 수 없다. 2번 인덱스의 값이 2보다 크기 때문에 서로 다른 원소를 포함하고 있는 정렬된 배열에서는 2번 인덱스 보다 큰 인덱스에서는 자신과 같은 배열의 값을 가질 수 없다. 2번 인덱스의 값이 3이라고 했다면 3에서는 3보다 큰 값이 나와야 하고, 4에서는 4보다 큰 값이 나올 수 밖에 없다.

```
5
-5 1 7 8 10
(0 1 2 3 4)
```

<br>

백트래킹 방식의 재귀로 풀이하여 mid 값에서 왼쪽 오른쪽으로 모두 탐색에서 값을 찾으려 했다.

<br>

두번째 풀이에서는 위에서 언급한 내용을 반영해서 mid 인덱스의 배열 값에 따라 탐색 종료, 왼쪽, 오른쪽을 구분해서 풀이했다.

<br>

### JavaScript

#### 첫번째 풀이

python 의 bisect 내장 라이브러리의 bisect_left, bisect_right 함수를 참고해서 javascript 로 bisectLeft, bisectRight 함수를 구현해서 풀이했다.

<br>

<참고>

https://soopeach.tistory.com/31

https://docs.python.org/ko/3/library/bisect.html

https://github.com/python/cpython/blob/3.11/Lib/bisect.py

