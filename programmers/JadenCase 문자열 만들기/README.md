# 프로그래머스

## JadenCase 문자열 만들기

공백이 두칸 이상인 경우가 있을 수 있는데 JadenCase 로 바꿀 경우 원래 공백은 그대로 유지해야 한다. 이 부분을 제대로 파악하지 못했다.

파이썬의 split 함수를 사용할 경우 split 의 인자를 공백 한 칸 ' ' 을 넣어주면 이 공백을 구분자로 split 이 수행된다. 만약에 인자로 아무것도 넣지 않을 경우 연속된 공백을 하나의 구분자로 간주한다.

```python
s = 'abc  def  ghi'

list_s_with_sep = s.split(' ')
# ['abc', '', 'def', '', 'ghi']

list_s_with_no_sep = s.split()
# ['abc', 'def', 'ghi']
```



<br>

<참고>

https://docs.python.org/3/library/stdtypes.html?highlight=split#str.split

