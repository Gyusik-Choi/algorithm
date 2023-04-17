# 이것이 코딩테스트다

## 챕터 12 8번 문자열 재정렬

구현 문제다.

정규표현식, 아스키코드, isalpha 함수(python) 등을 활용해서 풀이했다.

### 정규표현식

정규표현식은 정규표현식으로 문자와 숫자를 찾고 문자의 경우 오름차순 정렬하고 숫자의 경우 문자열로 배열 형태로 되어있어서 이를 숫자로 바꿔서 합을 구해줬다.

```python
import re
S = input()
a = re.findall('[A-Z]+', S)
b = re.findall('[A-Z]{1}', S)
c = re.findall('[A-Z]', S)

print(a)
print(b)
print(c)

# ['K', 'KA', 'CB']
# ['K', 'K', 'A', 'C', 'B']
# ['K', 'K', 'A', 'C', 'B']
```

<br>

'[A-Z]' 뒤에 +를 사용하면 하나 이상의 연속된 문자열을 하나로 저장하므로 이를 사용하지 않거나 +대신 {1}로 명시해줄 수 있다.

<br>

### 아스키코드

아스키코드는 알파벳 대문자는 65에서 90 사이다. 입력받은 값을 for 문으로 돌면서 65에서 90이면 문자열을 저장하는 배열에 담고 나머지는 숫자이므로 숫자를 담는 배열에 담았다. 문자열을 모은 배열은 오름차순 정렬하고, 숫자를 모든 배열은 문자열 형태로 원소들이 저장되어 있어서 숫자로 변환한 후에 합계를 구했다.

<br>

### isalpha

python 의 isalpha 함수는 알파벳 여부를 판단해준다. 다만 공백이 포함되면 알파벳만 있더라도 False 로 나오는 것을 주의해야 한다.

```python
alphabets = 'a b c'
print(alphabets.isalpha())
# False
```



```python
alphabets = 'abc'
print(alphabets.isalpha())
# True
```



<br>

<참고>

https://software-creator.tistory.com/32