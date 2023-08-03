# 프로그래머스

## 신규 아이디 추천

정규 표현식을 활용했다.

이번 문제를 풀이하면서 익힌 정규 표현식 내용을 몇 가지 정리하려고 한다.

<br>

### 특정 문자를 나타내는 표현

[] 와 \ 를 사용할 수 있다.

. 을 찾고 싶을 때 [.], \\. 둘 다 가능하다.

```python
import re
re.compile('[.]')
re.compile('\.')
```



<br>

### 반복 횟수

반복 횟수는 {} 로 정할 수 있다. 

최소 반복 횟수는 있는데 최대 반복 횟수는 정해지지 않았을 때도 있다. 이때는 {최소 반복 횟수,} 로 표현할 수 있다.

예를 들어 . 이 1회 이상 반복 하는 횟수를 찾는다면 아래와 같이 표현할 수 있다.

```python
import re
re.complie('\.{1,}')
```

<br>

다음과 같은 방법도 가능하다.

```python
import re
re.compile('\.+')
```

<br>

<참고>

https://codingspooning.tistory.com/entry/Python-%EC%A0%95%EA%B7%9C%ED%91%9C%ED%98%84%EC%8B%9D%EC%9C%BC%EB%A1%9C-%ED%95%9C%EA%B8%80-%EC%B6%94%EC%B6%9C%ED%95%98%EA%B8%B0-%EB%AC%B8%EC%9E%90%EC%97%B4-text-%EC%A0%84%EC%B2%98%EB%A6%AC

https://jjuha-dev.tistory.com/entry/Python-%EC%A0%95%EA%B7%9C%ED%91%9C%ED%98%84%EC%8B%9D-resub%EC%9D%84-%EC%9D%B4%EC%9A%A9%ED%95%9C-%EB%AC%B8%EC%9E%90%EC%97%B4-%EC%B9%98%ED%99%98%ED%95%98%EA%B8%B0

https://whitewing4139.tistory.com/167

https://wikidocs.net/4308#dot-n

