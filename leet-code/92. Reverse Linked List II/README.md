# LeetCode

## 92. Reverse Linked List II

### Python

root 노드를 생성해서 root.next 가 head 를 바라보도록 생성하고 추후에 root.next 를 리턴해서 root 를 제외한 head 부분만 포함된다.

그냥 head 를 리턴하는 것도 가능하지 않을까 싶었지만 첫번째 노드가 뒤집는 범위에 포함되면 head 가 전체 노드 중 마지막 노드를 가리키게 돼서 제대로된 값을 리턴할 수 없다.

start 와 end 는 가리키는 노드 자체가 바뀌지 않고 각각의 next 속성이 가리키는 노드가 바뀐다. 

temp 에는 start.next 를 대입하고 start.next 에는 end.next 를 대입하는데 이는 start.next.next 에 temp 를 대입하면서 노드를 뒤집는데 중요한 역할을 한다. start.next 는 end.next 를 따라서 앞으로 나아가는데 start.next.next  에 temp 가 대입 되면서 다시 start.next 를 start 와 바로 인접한 노드가 되도록 한다.

<br>

### Java

#### ReverseLinkedListII92

역순으로 뒤집은 연결 리스트 이전 구간, 역순으로 뒤집을 연결 리스트, 역순으로 뒤집은 연결 리스트 이후 구간 3개로 나눠서 진행했다.

이전 구간을 찾기 수월하도록 head 앞에 하나의 임시 노드를 추가해서 진행하고 임시 노드의 next 를 반환했다. 임시 노드를 사용하지 않으면 첫번째 노드부터 역순으로 뒤집을 경우 이전 구간을 null 로 설정해야 한다. 추후에 이전 구간과 역순으로 뒤집은 노드를 연결할 때 이전 구간이 null 이면 next 로 접근할 수 없다. 그리고 이전 구간이 null 이 아닌 경우도 처음에 null 로 초기화했기 때문에 NullPointerException 발생 가능성 때문에 IDE 에서는 경고를 띄우고, null 이 아니라는 조건절이 추가되야 하는 불편함이 있다.

이런 불편함을 임시 노드를 둬서 해결할 수 있었다. 임시 노드와 역순으로 뒤집은 노드가 연결되더라도 반환하는 값은 임시 노드의 이후 노드라서 상관없다.

<br>

#### ReverseLinkedListII92_2

leftNode 는 역순으로 뒤집은 연결 리스트의 이전 구간, prev 가 역순으로 뒤집은 연결 리스트, 그리고 node 는 역순으로 뒤집은 연결 리스트의 이후 구간을 나타낸다.

비록 3구간을 나타내는 변수들이 모두 이전 풀이처럼 존재하지만 이전 풀이와의 차이점은 역순으로 뒤집은 연결 리스트의 이후 구간을 별도로 찾는 작업을 하지 않는다.

<br>

#### ReverseLinkedListII92_3

교재의 풀이를 참고했다.

start 와 end 가 가리키는 노드는 바뀌지 않는다. start 는 위치를 고정하고 end 는 한칸씩 앞으로 이동한다. start 는 end 의 다음 노드와 연결한다. 그리고 연결된 end 다음 노드의 다음 노드를 start 의 한칸 앞의 노드를 바라보게 해서 위치를 변경한다.

<br>

#### ReverseLinkedListII92_4

노드를 뒤집은 후에 앞, 뒤 연결을 바꿔야 한다.

뒤집을 노드의 앞 노드는 뒤집혀서 맨 앞으로 오게된 노드를 바라봐야 하고, 뒤집혀서 맨 뒤로 오게된 노드는 뒤집을 노드의 뒤 노드를 바라봐야 한다.

뒤집을 노드의 앞 노드에 대한 참조를 prevRef 가 하고, 뒤집을 노드의 뒤 노드에 대한 참조를 next 가 한다.

<br>

#### ReverseLinkedListII92_5

ReverseLinkedListII92_4 와 동일한 방식으로 풀이했다.

<br>

### Kotlin

#### ReverseLinkedListII92

Java 의 ReverseLinkedListII92_4 풀이와 같은 방식으로 풀이했다.

<br>

<참고>

파이썬 알고리즘 인터뷰

자바 알고리즘 인터뷰



