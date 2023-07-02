# LeetCode

## 206. Reverse Linked List

### 206_reverse_linked_list.py

while 문을 이용해서 풀이했다. [234번 문제](https://leetcode.com/problems/palindrome-linked-list/) 에서 연결 리스트를 뒤집는데 사용한 방법을 그대로 적용했다.

입력으로 주어지는 연결 리스트 head 를 처음부터 마지막까지 순회하면서 head 값을 None 으로 초기화된 변수 rev 에 대입하고, rev.next 에 기존 rev 값을 대입한다.

<br>

<br>

<참고>

파이썬 알고리즘 인터뷰

