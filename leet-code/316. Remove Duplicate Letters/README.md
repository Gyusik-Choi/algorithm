# LeetCode

## [316. Remove Duplicate Letters](https://leetcode.com/problems/remove-duplicate-letters/)

### Java

#### RemoveDuplicateLetters316

교재의 풀이를 참고했다. 스택을 이용한 풀이다.

counter 변수는 각 문자의 갯수를 관리하고, complete 변수는 해당 문자를 처리했는지 여부를 관리하고, 그리고 stack 변수는 정답이 될 문자를 관리한다.

문자열 s 의 각 문자별 갯수를 counter 에 저장한 후 s 를 char array 로 변경해서 for 문을 돈다. counter 에서 for 문의 요소 갯수를 1 빼고 이미 완료처리된 문자면 다음 for 문의 요소로 넘어간다. 완료처리가 되지 않은 문자면 while 문을 돈다. while 문의 조건은 stack 이 비어있지 않고, stack 의 마지막 문자가 for 문의 요소보다 크면서 stack 의 마지막 문자가 아직 counter 에 남아 있는 경우(for 문의 이후 요소로 stack 의 마지막 문자가 나올 수 있는 경우)로 stack 에서 마지막 문자를 꺼내고 꺼낸 문자의 완료처리를 취소한다. 이어서 for 문의 요소를 완료처리하고 stack 에 넣는다.

stack 에 남은 문자를 while 문을 돌면서 StringBuilder 로 합치고 문자열로 변환하여 리턴한다.

<br>

#### RemoveDuplicateLetters316_2

교재의 풀이를 참고했다. 재귀를 활용한 풀이며 이해하기 어려웠다.

정렬을 지원하는 Set 인터페이스 구현체인 TreeSet 을 사용한다. TreeSet 으로 문자열 s 를 문자 단위로 정렬해서 중복을 제거한 집합으로 구한다.

집합을 for 문을 돌면서 해당 문자가 포함된 위치부터 잘라낸 접미사와 동일하면 해당 문자가 현재 s 에서 가장 앞에 나오는 문자라는 의미다. 해당 문자의 앞 문자들은 필요없다.

```
bbcaac
```

위의 문자열을 오름차순 정렬해서 TreeSet 으로 만들면 a, b, c 가 된다.

a, b, c 를 for 문을 돌면 a 의 suffix 가 aac 가 되고 정렬해서 Set 으로 만들면 a, c 라서 a, b, c 와 다르다. 그러나 b 의 suffix 가 bbcaac 가 되고 정렬해서 Set 으로 만들면 a, b, c 라서 a, b, c 와 동일하다. 

bbcaac 에서 가장 앞에 나오는 문자는 b 다. suffix 에서 b 를 제거한 문자를 재귀호출한다.

<br>

### Kotlin

#### RemoveDuplicateLetters316

RemoveDuplicateLetters316 을 java 에서 kotlin 으로 변환한 풀이다.

<br>

#### RemoveDuplicateLetters316_2

교재의 풀이를 참고했다. 이해하기 어려운 풀이였다.

java 의 RemoveDuplicateLetters316_2 와 동일한 방식으로 풀이했다.

중복을 제거하고 오름차순 정렬한 문자열과 특정 문자를 기준으로 해당 문자열을 중복을 제거해서 오름차순 정렬한 문자열이 동일하면 이 문자 이후의 문자열을 탐색하는 방식이다.

<br>

<참고>

자바 알고리즘 인터뷰

