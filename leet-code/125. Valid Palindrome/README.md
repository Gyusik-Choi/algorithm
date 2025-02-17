# LeetCode

## 125. Valid Palindrome

### Python

팰린드롬 여부를 확인하는 문제다. 팰린드롬은 영문자에서 대문자는 모두 소문자로 변환하고, 영숫자가 아닌 문자는 모두 제거한 후에 앞으로 읽은 값과 뒤로 읽은 값이 일치하는 경우를 나타낸다.

영문자 여부를 판단하기 위해 isalnum 문자열 메소드를 활용했다. isalnum 은 **alphanumeric**(영숫자) 값이면 True 를 반환하고 그렇지 않으면 False 를 반환한다.

영문자 여부를 판단한 후에 arr_s 배열에 문자를 소문자로 변경해서 넣었다.

그리고 arr_s 의 시작 인덱스 값을 front, 마지막 인덱스 값을 back 에 담고서 front 값이 back 보다 같거나 커지지 전까지 while 문을 돌면서 해당 front, back 인덱스의 문자열이 동일한지 비교해서 다르면 False 를 반환한다. while 문을 한번 순회한 후에 front 는 1을 더하고 back 은 1을 감소한다. while 문을 끝까지 돌면 True 를 반환한다.

<br>

### Java & Kotlin

정규표현식을 활용해서 풀이했다. 

정규표현식으로 알파벳과 숫자 형태 외의 문자열을 제거했다. 그리고 대소문자를 구분하지 않도록 모두 소문자로 변경했다.

이렇게 만든 문자열과 해당 문자열을 뒤집은 문자열을 비교해서 같으면 팰린드롬이다.

<br>

<참고>

https://docs.python.org/3/library/stdtypes.html?highlight=isalnum#str.isalnum

파이썬 알고리즘 인터뷰

자바 알고리즘 인터뷰

