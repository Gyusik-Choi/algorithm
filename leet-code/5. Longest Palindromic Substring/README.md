# LeetCode

## 5. Longest Palindromic Substring

투포인터를 활용해서 풀이했다. 가장 긴 팰린드롬 문자열을 찾는 문제다. 팰린드롬은 앞으로 읽은 것과 뒤로 읽어게 서로 같은 경우를 나타낸다.

길이가 홀수 길이일 수도 있고 짝수 길이일 수도 있어서 둘 다 탐색해야 한다. for 문을 돌면서 단어의 길이를 벗어나지 않는 범위 내에서 start, end 인덱스의 값이 서로 일치하면 start 는 1씩 줄이고, end 는 1씩 늘려나간다. while 문이 종료될때 이미 start, end 는 각각 1이 감소, 증가해서 리턴할 때는 이를 고려해야 한다. 

다만 주의할점은 리턴하는 문자열 슬라이싱의 인덱스를 start 는 1을 증가시키되 end 는 1을 감소시키면 안 된다. 슬라이싱의 끝 인덱스는 해당 인덱스의 앞까지 자르기 때문에 end 값으로 슬라이싱 하는게 end - 1 범위까지 슬라이싱을 하는 것과 같다.

<br>

### Java

#### LongestPalindromeSubstring5 

s 의 길이만큼 for 문을 돌면서 for 문의 요소를 기준으로 짝수, 홀수 팰린드롬을 모두 찾으려했다. 

팰린드롬을 찾으면서 findPalindrome 함수의 파라미터인 left, right 가 갱신될 때마다 substring 으로 문자열 값을 새로 구하는데 이게 시간이 느려지는 원인이 됐다.

<br>

#### LongestPalindromeSubstring5_2

교재의 풀이를 참고해서 substring 을 한번만 하도록 수정해서 시간을 10배 가까이 빠르게 할 수 있었다.

다만 인스턴스 변수를 사용해서 아래와 같이 호출할 경우 인스턴스 변수가 재활용돼서 에러가 발생했다. 물론 이는 리트코드에는 제출하는 것과는 관계가 전혀 없고, 단지 이렇게 호출을 할 경우만 에러가 발생하는 원인이나 함수 내에서 지역 변수를 사용하고 싶었다.

```java
LongestPalindromeSubstring5_3 solution3 = new LongestPalindromeSubstring5_3();
solution3.longestPalindrome("babad");
solution3.longestPalindrome("cbbd");
solution3.longestPalindrome("c");
solution3.longestPalindrome("cc");
solution3.longestPalindrome("cb");
```

<br>

#### LongestPalindromeSubstring5_3

인스턴스 변수가 아닌 함수 지역변수를 사용하도록 변경했다. 지역변수를 사용하기 위해 findPalindrome 함수에서 인스턴스 변수를 직접 수정하던 LongestPalindromeSubstring5_2 의 방법과 달리 left, right 값을 배열로 리턴한다.

<br>

####LongestPalindromeSubstring5_4

기존의 풀이와 달리 길이 1인 문자열에 대한 예외처리 없이 풀이했다.

<br>

### Kotlin

자바의 LongestPalindromeSubstring5_3 와 동일한 방식으로 풀이했다.

<br>

<참고>

파이썬 알고리즘 인터뷰

https://ko.wikipedia.org/wiki/%ED%9A%8C%EB%AC%B8

자바 알고리즘 인터뷰

