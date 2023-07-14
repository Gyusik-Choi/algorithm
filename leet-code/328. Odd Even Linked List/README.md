# LeetCode

## 328. Odd Even Linked List

처음에 head 와 odd 가 같은 노드를 바라본다. odd 는 계속 이동하지만 head 는 변하지 않는다. odd 가 맨 첫 노드를 더 이상 보고 있지 않아도 head 가 계속 맨 첫 노드를 보고 있다. head 가 맨 첫 노드를 계속 바라보고 있어서 odd 가 변경시킨 노드 연결 관계를 head 를 통해서 볼 수 있다.

even_head 와 even 도 head 와 odd 의 경우처럼 처음에 같은 노드를 바라보다가 even 은 계속 이동하지만 even_head 는 변하지 않는다. even_head 를 통해서 even 이 변경시킨 노드 연결 관계를 even_head 를 통해서 볼 수 있다.

head 와 odd, even_head 와 even 이 각각 쌍으로 구성된다. 쌍마다 각자 노드 시작부분 유지와 노드 연결관계 변경을 담당한다.

<br>

<참고>

파이썬 알고리즘 인터뷰

