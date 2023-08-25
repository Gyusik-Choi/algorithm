# 프로그래머스

## 정수 내림차순으로 배치하기

문자열로 정수 n 으로 변경하고, 이를 역순으로 정렬한 후에 join 메소드로 문자열로 만든 후 이를 다시 정수로 변환한 값을 리턴한다.

<br>

한가지 덫붙이자면 sorted 메소드는 인자로 리스트 뿐만 아니라 문자열도 가능하다.

```python
int(''.join(sorted(list(str(n)), reverse=True)))
```

<br>

위의 코드처럼 문자열을 리스트로 변환한 후에 sorted 메소드로 정렬하지 않고 문자열을 sorted 메소드로 정렬할 수 있다. 정렬 후에는 리스트가 반환된다.

```python
int(''.join(sorted(str(n), reverse=True)))
```

