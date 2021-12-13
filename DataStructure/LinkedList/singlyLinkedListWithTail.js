const Node = function(value, next = null) {
    this.value = value
    this.next = next
}

const SinglyLinkedList = function() {
    this.head = new Node(null)
    this.tail = this.head
}

SinglyLinkedList.prototype.isEmpty = function() {
    return this.head.value === null && this.tail.value === null
}

SinglyLinkedList.prototype.add = function(value) {
    if (this.isEmpty()) {
        this.head = new Node(value)
        this.tail = this.head
    } else {
        const tail = this.tail
        this.tail = new Node(value)
        tail.next = this.tail
    }
}

SinglyLinkedList.prototype.remove = function() {
    if (this.isEmpty()) {
        console.log("empty")
        return false
    } else {
        const removeItem = this.tail.value
        // node 가 하나일때
        // value 만 비교하면 하나일때가 아니더라도 head와 tail이 같을 수 있다
        // 그러나 value 뿐만 아니라 next 프로퍼티의 값도 같으려면 node 가 하나여야 한다
        // node 가 하나일때 next 프로퍼티의 값이 head와 tail 모두 null
        if (this.head === this.tail) {
            this.head = new Node(null)
            this.tail = this.head
        } else {
            let cur = this.head

            // doubleLinkedList 였다면 tail에서 prev를 끝어주고 prev에서 next를 null로 바꾸면 되지만
            // singlyLinkedList는 맨 마지막 node의 바로 앞 node를 찾아서 next를 null로 해야하므로
            // head에서 부터 순차적으로 가야한다
            while (cur.next.next !== null) {
                cur = cur.next
            }
            cur.next = null
            // this.tail을 재설정해줘야 한다
            // 그러지 않으면 떨어져나간 기존의 tail이 연결관계만 끊긴채 tail로 남아있는다
            this.tail = cur
            console.log(cur)
        }
        
        console.log(removeItem)
        return removeItem
    }
}

const sll = new SinglyLinkedList()
sll.add(1)
sll.add(2)
sll.add(3)
sll.add(4)
sll.add(5)
sll.remove()
console.log(sll)
