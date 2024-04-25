# LeetCode

## [461. Hamming Distance](https://leetcode.com/problems/hamming-distance/)

해밍 거리를 구하는 문제다.

해밍 거리는 같은 길이의 문자열 등에서 서로 다른 기호가 몇개가 있는지를 나타낸다.

문제에서는 문자열이 아닌 정수 2개가 주어지고 정수의 비트가 몇개가 다른지 찾아야 한다.

<br>

XOR 연산을 활용해서 풀이했다. 

XOR 연산은 비트가 서로 다르면 1, 같으면 0이다. XOR 연산을 한 후에 1의 갯수를 세면 된다.

<br>

XOR 연산으로 ^(caret) 연산자를 사용할 수 있고 또 다른 방법으로는 operator 모듈의 xor 함수를 사용할 수도 있다. operator 모듈의 xor 함수는 내부적으로 ^ 연산자를 사용한다.

<br>

<참고>

https://ko.wikipedia.org/wiki/%ED%95%B4%EB%B0%8D_%EA%B1%B0%EB%A6%AC

https://docs.python.org/3/library/stdtypes.html#str.count

https://docs.python.org/3/library/operator.html

https://github.com/python/cpython/blob/3.9/Lib/operator.py

