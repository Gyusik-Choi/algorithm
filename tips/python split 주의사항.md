# split 주의사항

문자열 값을 분리해서 리스트로 만들때 split 메소드를 사용할 수 있다.

그런데 문자열 값이 붙어있어서 공백이 없는 문자열을 하나씩 나눌 때 주의해야 한다.

```python
value = '12345'
list(value)
# ['1', '2', '3', '4', '5']
list(value.split(''))
# ValueError: empty separator
```

<br>

 위에서 보듯이 '12345' 인 문자열은 split 을 따로 쓰지 않고 바로 list 로 감싸주면 하나씩 분리되어 리스트로 변환된다.

<br>

<참고>

https://codesample-factory.tistory.com/1755

