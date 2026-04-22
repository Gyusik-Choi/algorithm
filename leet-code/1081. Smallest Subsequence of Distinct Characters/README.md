# LeetCode

## [1081. Smallest Subsequence of Distinct Characters](https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/)

### Java

#### SmallestSubsequenceOfDistinctCharacters1081

스택을 활용해서 풀이했다.

문자열을 순회하면서 스택의 최상단 요소보다 현재 문자가 더 작고 스택의 최상단 요소가 현재 문자 이후에 나올 예정이라면 스택의 최상단 요소를 제거한다. 

스택의 최상단 요소가 현재 문자 이후에 나올 수 있으면 스택에서 제거하고 이후에 스택에 추가하면 알파벳 순서상 더 작은 조건을 만족할 수 있다.

<br>

<참고>

https://leetcode.com/problems/remove-duplicate-letters/

자바 알고리즘 인터뷰

