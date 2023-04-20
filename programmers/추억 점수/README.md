# 프로그래머스

## 추억 점수

defaultdict 를 활용했다.

name 을 key, yearning 을 value 로 하는 딕셔너리를 만들면 단점이 이 딕셔너리에 존재하지 않는 key 에 접근하면 KeyError 가 발생한다. 이를 방지하려고 in 을 통해서 딕셔너리에 해당하는 key 가 존재하는지를 검사해야 한다. 이를 통해 O(1) 에 value 를 찾을 수 없고 O(N) 에 value 를 찾게 된다.

defaultdict 를 사용하면 존재하지 않는 키에 접근했을 때 에러가 발생하지 않고 default 로 적용한 값이 설정된다. 주의할점은 defaultdict 를 생성할때 default 로 사용할 값을 넣어줘야 한다. 공식문서에는 이 기본값을 [`default_factory`](https://docs.python.org/3/library/collections.html?highlight=defaultdict#collections.defaultdict.default_factory) 라고 소개한다. default 로 int 를 적용하면 존재하지 않는 key 에 접근시 해당 key 의 value 로 0을 만든다. KeyError 가 발생하지 않는다.

```python
from collections import defaultdict


default = defaultdict(int)
print(default['python'])
# 0

dic = dict()
print(dic['python'])
# KeyError
```

<br>

<참고>

https://docs.python.org/3/library/collections.html?highlight=defaultdict#collections.defaultdict