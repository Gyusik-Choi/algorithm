# 백준

## 인사성 밝은 곰곰이

ENTER 를 기준으로 고유한 사용자가 몇 명인지 누적합을 구해야 한다.

ENTER 로 각 요소를 나눈 후에 요소마다 set 으로 고유한 사용자가 몇 명인지 구하고 reduce 로 누적합을 구했다.

ENTER 로 나누면 ENTER 요소는 사라지지 않고 리스트에 빈 문자열로 남으며 잘라진 요소의 앞이나 뒤에 공백 문자가 생긴다.

```python
chats = ['ENTER', 'abc', 'def']
print(' '.join(chats).split('ENTER'))
# ['', ' abc def']
# ENTER 는 '' 가 되고 abc, def 는 하나로 묶이되 앞에 공백 문자가 생겨서 ' abc def' 가 된다
```

<br>

```python
chats = ['ENTER', 'abc', 'def', 'ENTER']
print(' '.join(chats).split('ENTER'))
# ['', ' abc def ', '']
# ENTER 는 '' 가 되고 abc, def 는 하나로 묶이되 앞과 뒤에 공백 문자가 생겨서 ' abc def ' 가 된다
```

<br>

빈 문자열은 filter 로 제거하고 앞이나 뒤의 공백 문자는 strip 으로 제거한다.

