# LeetCode

## 206. Reverse Linked List

### Python

#### 206_reverse_linked_list.py

while 문을 이용해서 풀이했다. [234번 문제](https://leetcode.com/problems/palindrome-linked-list/) 에서 연결 리스트를 뒤집는데 사용한 방법을 그대로 적용했다.

입력으로 주어지는 연결 리스트 head 를 처음부터 마지막까지 순회하면서 head 값을 None 으로 초기화된 변수 rev 에 대입하고, rev.next 에 기존 rev 값을 대입한다.

<br>

#### 206_reverse_linked_list_2.py

재귀를 활용했다. 교재의 풀이법을 이해하기가 쉽지 않았다.

파라미터가 2개가 필요해서 중첩 함수로 구현했다. 중첩함수에 연결 리스트와 None 을 인자로 넣어준다. 중첩함수에서 연결 리스트는 하나씩 next 를 호출하면서 None 이 될때까지 이어가고, 연결 리스트의 next 값으로 None 을 대입한다. 다시 중첩 함수를 호출할때 연결 리스트의 다음 노드와 현재 연결 리스트(next 가 업데이트 된 노드) 를 인자로 넣는다. 이를 연결 리스트가 마지막 노드의 next 까지 호출해서 None 이 될 때까지 반복한다.

<br>

### Java

#### ReverseLinkedList206

while 문을 사용해서 반복 구조로 풀이했다.

<br>

#### ReverseLinkedList206_2

재귀 구조로 풀이했다. head 의 마지막 노드까지 재귀호출을 한 후 head 의 첫번째 요소를 재귀호출에서 리턴받은 노드의 맨 마지막에 연결한다.

head 가 아래와 같을때 다음과 같은 형태로 역순 연결리스트를 만들어간다

```
head 1 -> 2 -> 3 -> 4 -> 5
```

<br>

```
head 4 -> 5
next 5
prev 4

next 4 <- 5
```

<br>

```
// next 를 맨 마지막까지 이동하면서 
// next 의 참조는 4 <- 5 를 유지할 수 있도록
// cur 변수에 next 를 할당한 후
// cur 를 마지막까지 이동해서 3 을 연결하고
// next 를 반환한다
head 3 -> 4 -> 5
next 4 <- 5
prev 3

next 3 <- 4 <- 5
```

<br>

```
head 2 -> 3 -> 4 -> 5
next 3 <- 4 <- 5
prev 2

next 2 <- 3 <- 4 <- 5
```

<br>

```
head 1 -> 2 -> 3 -> 4 -> 5
next 2 -> 3 <- 4 <- 5
prev 1

next 1 <- 2 <- 3 <- 4 <- 5
```

<br>

#### ReverseLinkedList206_3

교재의 풀이를 참고했다. ReverseLinkedList206_2 의 풀이와 달리 맨 마지막까지 재귀호출로 호출 스택을 쌓지 않는다.

노드의 다음 요소를 재귀호출하면 해당 호출스택에서 역순으로 노드를 뒤집은 후 리턴으로 해당 호출스택은 종료하고 다음 재귀호출로 넘어간다.

<br>

#### ReverseLinkedList206_4

ReverseLinkedList206 과 거의 유사한 방식으로 풀이했다.

ReverseLinkedList206 과 달리 cur.next 를 prev 에 붙이지 않고, prev.next 를 직전 prev 와 연결한다.

<br>

<참고>

파이썬 알고리즘 인터뷰

자바 알고리즘 인터뷰