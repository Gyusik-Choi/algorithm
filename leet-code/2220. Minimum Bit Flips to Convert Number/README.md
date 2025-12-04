# LeetCode

## [2220. Minimum Bit Flips to Convert Number](https://leetcode.com/problems/minimum-bit-flips-to-convert-number/)

### Java

#### MinimumBitFlipsToConvertNumber2220

[해당 문제](https://leetcode.com/problems/hamming-distance/description/) 의 웹페이지에서 이 문제가 동일한 유형의 문제라고 소개하고 있다.

이 문제는 서로 다른 비트의 수를 구하는 문제다. 2진수로 변환해서 자릿수마다 동일 여부를 비교할 수도 있으나 XOR 연산을 이용하면 좀 더 간단하게 풀이할 수 있다.

XOR 연산은 서로 다른 비트의 경우 1이 되기 때문에 XOR 연산을 수행한 뒤 1의 갯수를 구하면 된다. Java 에서는 Integer 클래스의 bitCount 메소드가 2진수의 1의 갯수를 세는 기능을 제공한다.

<br>

<참고>

자바 알고리즘 인터뷰

