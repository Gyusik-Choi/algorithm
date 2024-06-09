# 프로그래머스

## 접미사인지 확인하기

### 첫번째 풀이

[접두사인지 확인하기](https://school.programmers.co.kr/learn/courses/30/lessons/181906) 문제와 유사하게 리스트 슬라이싱을 활용하려 했다.

접미사 여부를 확인해야 해서 my_string 을 뒤집고 is_suffix 와 일치 여부를 판단하려 했으나 오답이 나왔다. 간과한 부분이 있었는데 my_string 을 역순으로 뒤집어서 is_suffix 와 비교하려면 is_suffix 도 역순으로 뒤집어야 한다.

<br>

```python
my_string = "abcde"
is_suffix = "de"
# my_string 을 역순으로 뒤집으면 edcba
```

위의 예시와 같이 abcde 를 역순으로 뒤집으면 edcba 가 된다. edcba 를 de 의 길이인 2만큼 edcba 를 슬라이싱하면 ed 가 된다. ed 와 de 를 비교하면 일치하지 않는다. 역순으로 뒤집은 문자열과 역순으로 뒤집지 않은 문자열을 비교하기 때문에 제대로 정답을 구할 수 없었다.

<br>

정답을 구하기 위해서는 my_string 을 역순으로 뒤집어서 문자열을 잘라낸 후 다시 역순으로 뒤집어서 is_suffix 와 비교하거나 is_suffix 를 역순으로 뒤집어서 비교하면 된다.

<br>

### 두번째 풀이

str 클래스의 내장 메소드인 endswith 으로 풀이할 수 있다.

endswith 은 대상 문자열이 인자로 넣은 문자열로 끝나는지를 판단하므로 접미사를 찾을 때 사용할 수 있다.

<br>

<참고>

https://school.programmers.co.kr/learn/courses/30/lessons/181906

https://yoonhwis.tistory.com/26

https://docs.python.org/3/library/stdtypes.html#str.endswith

