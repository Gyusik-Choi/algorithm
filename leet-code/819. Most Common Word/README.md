# LeetCode

## 819. Most Common Word

### 819_most_common_word.py

영문자가 아닌 경우에 모두 공백으로 변경한다. 그리고 모든 글자를 소문자로 바꾸고 공백을 기준으로 분리해서 리스트 값을 얻는다.

리스트를 순회하면서 banned 에 속하지 않은 단어들의 갯수를 센다. 

갯수가 가장 많은 단어를 리턴한다.

<br>

### 819_most_common_word.dart

819_most_common_word.py 와 같은 방식으로 풀이했다.

<br>

### Java 풀이

두번째 풀이에서는 교재의 코드를 참고해서 정규 표현식과 HashMap 의 값을 기준으로 키를 구하는 코드를 간소화할 수 있었다.

정규 표현식은 알파벳이나 숫자가 아닌 문자열을 제거하기 위해 \\\W 를 사용했다. 소문자 w를 사용해서 \\\w 는 알파벳이나 숫자를 나타낸다. w를 대문자인 W로 나타내면 이의 부정 표현이 돼서 알파벳이나 숫자가 아닌 수를 나타낸다.

HashMap 에서 가장 큰 값을 갖는 키를 찾아야 했는데, 교재의 풀이를 참고해서 한줄로 줄일 수 있었다.

<br>

<참고>

https://docs.python.org/3.8/library/stdtypes.html#str.split

파이썬 알고리즘 인터뷰

자바 알고리즘 인터뷰

https://hstory0208.tistory.com/entry/Java%EC%9E%90%EB%B0%94-%EC%A0%95%EA%B7%9C%EC%8B%9DRegular-Expression-%EC%82%AC%EC%9A%A9%EB%B2%95-1

