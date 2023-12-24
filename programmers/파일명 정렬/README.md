# 프로그래머스

## 파일명 정렬

### 첫번째 풀이

파일을 head, number, tail 로 분리하고 파일 원본도 포함해서 리스트로 묶었다. 이 리스트에는 파일 원본도 포함했다. 파일 원본은 정렬 후에 원본 값으로 리턴하기 위해 사용했다.

```python
[head, number, tail, 파일]
```

<br>

head, number, tail 로 분리하기 위해 isdigit 문자열 메소드를 사용했다. 

number 는 head 뒤에 나오기 때문에 숫자가 처음 등장하면 숫자가 처음 등장한 인덱스 뒤까지가 head 가 된다. tail 에도 숫자가 나올 수 있어서 number 와 구분하기 위해 숫자가 처음 나온 시점부터 인덱스를 구해서 연속한 숫자만 number 로 구하기 위해 현재 인덱스와 직전 숫자가 나온 인덱스의 차이가 1인 경우만 number 로 넣었다.

<br>

### 두번째 풀이

정규표현식을 활용했다. 정규표현식을 통해 head, number, tail 을 보다 간결한 코드로 분리할 수 있었다.

<br>

<참고>

https://docs.python.org/3/library/stdtypes.html#str.isdigit

https://school.programmers.co.kr/learn/courses/30/lessons/17686/solution_groups?language=python3

https://velog.io/@geonhwi/%EC%A0%95%EA%B7%9C%ED%91%9C%ED%98%84%EC%8B%9D-2

https://velog.io/@seob/regex-is-easy

