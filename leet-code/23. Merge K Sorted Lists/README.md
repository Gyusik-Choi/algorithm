# LeetCode

## 23. Merge K Sorted Lists

### Python

#### 우선순위 큐

heapq 모듈을 사용해서 우선순위 큐를 활용했다.

lists 리스트를 for 문을 돌면서 각 연결 리스트 객체를 heapq 모듈의 heappush 메소드를 이용해서 리스트에 담았다.

리스트에 담을 때 ListNode 의 val 과 ListNode 객체 자체 뿐만 아니라 lists 의 인덱스도 넣었다.

ListNode 의 val 이 중복돼서 에러가 발생하는 것을 방지하기 위해 lists 의 인덱스를 넣었다.

<br>

리스트에 넣은 후 heapq 모듈의 heappop 메소드로 최소 val 을 가진 요소를 꺼내준다. 

이때 ListNode 의 next 에 다음 ListNode 가 있다면 해당 객체를 다시 heappush 메소드를 이용해서 리스트에 넣어서 모든 연결리스트 노드가 리스트에 빠짐없이 들어갈 수 있도록 한다.

<br>

#### 연결 리스트

head 변수에 ListNode 인스턴스를 할당하고 cur 변수에 head 를 할당했다.

cur 변수의 next 키에 노드를 연결하고 head 는 연결 리스트의 시작 부분을 계속 바라보고 있다. 

head 의 next 를 리턴하면 빈 값이 있는 연결 리스트 시작 부분을 제외하고 cur 가 이어붙인 부분만 리턴할 수 있다.

<br>

### Java

교재의 풀이를 참고했다.

우선순위 큐를 활용하면 보다 쉽게 풀이할 수 있다. 우선순위 큐의 정렬 기준을 Comparator 클래스로 넣어서 정할 수 있다. Comparator 클래스를 정의하는 몇 가지 방법이 있다.

<br>

#### 익명 클래스

```java
PriorityQueue<ListNode> pq = new PriorityQueue<>(new Comparator<ListNode>() {
  @Override
  public int compare(ListNode o1, ListNode o2) {
    return o1.val - o2.val;
  }
});
```

<br>

#### 람다식

```java
PriorityQueue<ListNode> pq = new PriorityQueue<>((o1, o2) -> o1.val - o2.val);
```

<br>

### comparingInt 스태틱 메소드

```java
PriorityQueue<ListNode> pq = new PriorityQueue<>(Comparator.comparingInt(o -> o.val));
```

<br>

우선순위 큐에 대한 정렬 기준을 설정한 후 lists 를 for 문을 돌면서 하나씩 노드를 우선순위 큐에 넣는다. ListNode 가  null 일 수 있어서 null 이 아닌 경우만 우선순위 큐에 넣는다.

우선순위 큐에서 노드를 꺼내고 head 노드의 next 에 우선순위 큐에서 꺼낸 노드를 연결하고, 꺼낸 노드의 next 가 null 이 아니면 꺼낸 노드의 next 노드를 다시 우선순위 큐에 넣는다.

root, head 두 가지 변수를 사용했는데 root 는 전체 노드에 대한 참조를 유지하기 위한 변수고, head 는 root 와 같은 참조를 보다가 우선순위 큐에서 꺼낸 노드를 연결하기 위해 한칸씩 이동하는 노드다.

모든 노드를 연결하면 root 의 next 노드를 리턴한다.

<br>

<참고>

파이썬 알고리즘 인터뷰

자바 알고리즘 인터뷰

