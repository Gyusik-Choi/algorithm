# LeetCode

## 328. Odd Even Linked List

### Python

처음에 head 와 odd 가 같은 노드를 바라본다. odd 는 계속 이동하지만 head 는 변하지 않는다. odd 가 맨 첫 노드를 더 이상 보고 있지 않아도 head 가 계속 맨 첫 노드를 보고 있다. head 가 맨 첫 노드를 계속 바라보고 있어서 odd 가 변경시킨 노드 연결 관계를 head 를 통해서 볼 수 있다.

even_head 와 even 도 head 와 odd 의 경우처럼 처음에 같은 노드를 바라보다가 even 은 계속 이동하지만 even_head 는 변하지 않는다. even_head 를 통해서 even 이 변경시킨 노드 연결 관계를 even_head 를 통해서 볼 수 있다.

head 와 odd, even_head 와 even 이 각각 쌍으로 구성된다. 쌍마다 각자 노드 시작부분 유지와 노드 연결관계 변경을 담당한다.

<br>

### Java

#### OddEvenLinkedList328

재귀를 활용했다.

ListNode 가 null 이거나 ListNode 의 next 가 null 일 때까지 현재 노드의 다음 다음 노드를 재귀호출한다. ListNode 가 null 이거나 ListNode 의 next 가 null 인 조건을 만족하면 배열에 node 와 null 을 담아서 리턴한다. 배열의 0번 인덱스는 홀수노드, 1번 인덱스는 짝수노드가 된다.

현재 노드와 0번 인덱스를 연결하고 다음 노드와 1번 인덱스를 연결한다. 그리고 다시 현재 노드와 다음 노드를 배열에 담아 리턴한다.

마지막에는 0번 인덱스와 1번 인덱스를 연결하고 head 를 반환한다.

<br>

#### OddEvenLinkedList328_2

처음에는 교재의 풀이와 다르게 접근(OddEvenLinkedList328_Circular_Reference)했는데 순환 참조가 발생했다. 

![circular](circular.jpg)

odd 와 even 을 나눠서 while 문을 진행했는데 odd 가 바뀌면서 head 도 바뀌고 head 의 다음 노드를 참조하던 even 도 영향을 주는데 이를 간과했다.

교재의 풀이를 참고하여 while 문을 한번만 돌면서 순환 참조를 해결했다.

<br>

#### OddEvenLinkedList328_3

while 문에서 head 의 길이가 홀수, 짝수 여부에 따라 상황이 조금 달라져서 짝수인 경우에 대해 예외 처리를 했다.

head 가 홀수인 경우 while 문 안에서 odd 노드는 맨 마지막까지 이동하고, even 노드는 null 이 된다. 별도의 예외처리 없이 while 문을 빠져나와서 odd.next 에 even 의 시작 노드를 참조하는 evenRef 를 할당하면 된다.

반면에 head 가 짝수인 경우 while 문 안에서 odd 노드는 맨 마지막에서 한칸 앞까지 이동하고, even 노드는 맨 마지막까지 이동한다. 이때 odd.next 가 even 을 참조하지 않으면서 odd, even 노드가 더 이동하지 않도록 예외처리를 한다. even 노드가 null 이 아니면서 even.next 노드가 null 인 상황이면 odd.next 는 even 을 참조하지 않도록 null 을 할당하고 while 문을 break 로 빠져나온다.

<br>

<참고>

파이썬 알고리즘 인터뷰

