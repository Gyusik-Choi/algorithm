# LeetCode

## 344. Reverse String

해당 문제의 조건은 문자열을 뒤집되 리턴하지 않고 reverseString 함수의 파라미터 s 자체를 변환해야 한다.

front, back 을 0, s의 길이 - 1로 각각 설정한 후에 front 가 back 보다 같아지기 전까지 front, back 인덱스 값을 서로 교환한다.

<br>

### Kotlin

#### ReverseString344

kotlin 은 scope function 중 하나인 also 를 사용해서 한줄로 서로 다른 리스트 요소간의 위치를 바꿀 수 있다.

scope function 에는 also 외에 let, run, with, apply 등이 있고, 이 함수들에 대한 사용법은 추가 학습이 필요하다.

<br>

<참고>

자바 알고리즘 인터뷰

https://kotlinlang.org/docs/scope-functions.html

