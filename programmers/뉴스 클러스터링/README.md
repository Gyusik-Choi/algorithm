# 프로그래머스

## 뉴스 클러스터링

자카드 유사도를 구하는 문제다.

문자열을 2글자씩 잘랐을때 자른 문자열이 영문자로만 구성된 경우 유효한 집합의 원소가 된다.

for 문을 돌면서 리스트 슬라이싱으로 문자열을 자를 수 있는데 대소문자를 구분하지 않는다고 해서 모두 소문자로 처리했다. 또한 영문자로만 구성 됐는지 확인하기 위해 정규표현식을 사용했다.

<br>

```python
import re


pattern = re.compile('[a-z]{2}')
print(re.findall(pattern, 'a+'))
# []
```

정규표현식의 패턴을 '[a-z]' 뒤에 {2} 를 붙여서 '[a-z]{2}' 로 하면 영소문자가 반드시 2글자 반복인 경우만 찾는다.

<br>

```
집합 A와 집합 B가 모두 공집합일 경우에는 나눗셈이 정의되지 않으니 따로 J(A, B) = 1로 정의한다.
```

문제에서 위와 같은 조건이 있어서 두 집합이 공집합인 경우만 1로 처리하려 했으나 문제의 의도는 그게 아니었다. 공집합인 경우만 1로 하는게 아니라 나눗셈이 정의되지 않는 경우를 1로 해야 한다.

0으로 나누면 나눗셈이 정의되지 않는다. 합집합이 0인 경우 1로 처리해야 한다.

<br>

```python
from collections import Counter


a = 'aaa'
b = 'aaaaa'
a_counter = Counter(a)
b_counter = Counter(b)
print(a_counter | b_counter)
# Counter({'a': 5})
```

딕셔너리 대신 Counter 모듈을 사용하면 집합 요소의 갯수를 세거나 교집합, 합집합을 구하는 것을 훨씬 쉽게 할 수 있다.

<br>

<참고>

파이썬 알고리즘 인터뷰

https://nachwon.github.io/regular-expressions/

