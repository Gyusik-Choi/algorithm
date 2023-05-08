# Leet Code

## 819. Most Common Word

### 819_most_common_word.py

영문자가 아닌 경우에 모두 공백으로 변경한다. 그리고 모든 글자를 소문자로 바꾸고 공백을 기준으로 분리해서 리스트 값을 얻는다.

리스트를 순회하면서 banned 에 속하지 않은 단어들의 갯수를 센다. 

갯수가 가장 많은 단어를 리턴한다.

<br>

### 819_most_common_word.dart

819_most_common_word.py 와 같은 방식으로 풀이했다.

<br>

<참고>

https://docs.python.org/3.8/library/stdtypes.html#str.split

