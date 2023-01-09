// Double Linked List 형태로 구현했다
// Singly Linked List 의 경우는 Stack 에서 제거할때 마지막 요소에서 하나 앞의 요소를 찾아야 한다
// 이러면 head 에서부터 순차적으로 탐색해야 한다
// Stack 이 길어질수록 탐색에 많은 시간이 소요되므로
// tail 에서 바로 prev 노드를 찾을 수 있도록 Double Linked List 형태로 구현했다
// 앞서 파이썬으로 구현한 Stack 은 Singly Linked List 형태로 구현해서
// head 를 추가하는 노드로 교체해주면서 삭제시에는 head 에서 제거하면서 삭제는 빠르게 할 수 있지만
// 추가할때마다 head 를 교체해줘야 하는 번거로움이 있다

const Node = function(value, prev = null, next = null) {
    this.value = value
    this.prev = prev
    this.next = next
}

const Stack = function() {
    this.head = new Node(null)
    this.tail = this.head
}

Stack.prototype.isEmpty = function() {
    return this.head.value === null && this.tail.value === null
}

Stack.prototype.add = function(value) {
    if (this.isEmpty()) {
        this.head = new Node(value)
        this.tail = this.head
    } else {
        const tail = this.tail
        this.tail = new Node(value, tail)
        tail.next = this.tail
    }
}

Stack.prototype.remove = function() {
    if (this.isEmpty()) {
        return false
    } else {
        const popNode = this.tail.value

        if (this.head === this.tail) {
            this.head = new Node(null)
            this.tail = this.head
        } else {
            this.tail = this.tail.prev
            this.tail.next = null
        }
        return popNode
    }
}

Stack.prototype.getStack = function() {
    let stack = []
    let cur = this.head

    while (cur) {
        stack.push(cur.value)
        cur = cur.next
    }

    console.log(stack)
    return stack
}

const s = new Stack()
s.add(1)
s.add(2)
s.remove()
s.add(2)
s.add(3)
s.add(4)
s.add(5)
s.getStack()
