# LeetCode

## 206. Reverse Linked List

### 206_reverse_linked_list.py

while 문을 이용해서 풀이했다. [234번 문제](https://leetcode.com/problems/palindrome-linked-list/) 에서 연결 리스트를 뒤집는데 사용한 방법을 그대로 적용했다.

입력으로 주어지는 연결 리스트 head 를 처음부터 마지막까지 순회하면서 head 값을 None 으로 초기화된 변수 rev 에 대입하고, rev.next 에 기존 rev 값을 대입한다.

<br>

### 206_reverse_linked_list_2.py

재귀를 활용했다. 교재의 풀이법을 이해하기가 쉽지 않았다.

파라미터가 2개가 필요해서 중첩 함수로 구현했다. 중첩함수에 연결 리스트와 None 을 인자로 넣어준다. 중첩함수에서 연결 리스트는 하나씩 next 를 호출하면서 None 이 될때까지 이어가고, 연결 리스트의 next 값으로 None 을 대입한다. 다시 중첩 함수를 호출할때 연결 리스트의 다음 노드와 현재 연결 리스트(next 가 업데이트 된 노드) 를 인자로 넣는다. 이를 연결 리스트가 마지막 노드의 next 까지 호출해서 None 이 될 때까지 반복한다.

<br>

<참고>

파이썬 알고리즘 인터뷰

