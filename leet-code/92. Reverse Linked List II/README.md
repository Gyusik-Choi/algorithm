# LeetCode

## 92. Reverse Linked List II

root 노드를 생성해서 root.next 가 head 를 바라보도록 생성하고 추후에 root.next 를 리턴해서 root 를 제외한 head 부분만 포함된다.

그냥 head 를 리턴하는 것도 가능하지 않을까 싶었지만 첫번째 노드가 뒤집는 범위에 포함되면 head 가 전체 노드 중 마지막 노드를 가리키게 돼서 제대로된 값을 리턴할 수 없다.

start 와 end 는 가리키는 노드 자체가 바뀌지 않고 각각의 next 속성이 가리키는 노드가 바뀐다. 

temp 에는 start.next 를 대입하고 start.next 에는 end.next 를 대입하는데 이는 start.next.next 에 temp 를 대입하면서 노드를 뒤집는데 중요한 역할을 한다. start.next 는 end.next 를 따라서 앞으로 나아가는데 start.next.next  에 temp 가 대입 되면서 다시 start.next 를 start 와 바로 인접한 노드가 되도록 한다.

<br>

<참고>

파이썬 알고리즘 인터뷰

