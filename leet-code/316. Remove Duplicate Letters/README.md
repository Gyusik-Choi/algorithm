# LeetCode

## [316. Remove Duplicate Letters](https://leetcode.com/problems/remove-duplicate-letters/)

### Java

#### RemoveDuplicateLetters316

교재의 풀이를 참고했다. 스택을 이용한 풀이다.

counter 변수는 각 문자의 갯수를 관리하고, complete 변수는 해당 문자를 처리했는지 여부를 관리하고, 그리고 stack 변수는 정답이 될 문자를 관리한다.

문자열 s 의 각 문자별 갯수를 counter 에 저장한 후 s 를 char array 로 변경해서 for 문을 돈다. counter 에서 for 문의 요소 갯수를 1 빼고 이미 완료처리된 문자면 다음 for 문의 요소로 넘어간다. 완료처리가 되지 않은 문자면 while 문을 돈다. while 문의 조건은 stack 이 비어있지 않고, stack 의 마지막 문자가 for 문의 요소보다 크면서 stack 의 마지막 문자가 아직 counter 에 남아 있는 경우(for 문의 이후 요소로 stack 의 마지막 문자가 나올 수 있는 경우)로 stack 에서 마지막 문자를 꺼내고 꺼낸 문자의 완료처리를 취소한다. 이어서 for 문의 요소를 완료처리하고 stack 에 넣는다.

stack 에 남은 문자를 while 문을 돌면서 StringBuilder 로 합치고 문자열로 변환하여 리턴한다.

<br>

<참고>

자바 알고리즘 인터뷰

