const Node = function(value, prev = null, next = null) {
    this.value = value
    this.prev = prev
    this.next = next
}

const Queue = function() {
    this.head = new Node(null)
    this.tail = this.head
    this.length = 0
}

Queue.prototype.isEmpty = function() {
    if (this.length === 0) {
    // if (this.head.value === null && this.tail.value === null) {
        return true
    }
    return false
}

Queue.prototype.enQueue = function(item) {
    if (this.isEmpty()) {
        this.head = new Node(item)
        this.tail = this.head
    } else {
        let tail = Pthis.tail
        this.tail = new Node(item, tail)
        tail.next = this.tail
    }
    this.length += 1
}

Queue.prototype.deQueue = function() {
    if (this.isEmpty()) {
        console.log("queue is empty")
        return
    } else {
        let popNode = ''
        // 이 코드로 큐에 숫자가 1개만 있을 때를 다루려고 했으나 여러개 있어도 맨앞과 맨뒤의 숫자가 같으면 걸릴 수 있으므로 좋지 않은 코드라고 생각해서 수정했다
        // length 프로퍼티를 추가해서 보다 명료하게 숫자가 1개만 있는 경우를 나타내도록 했다
        // if (this.head.val === this.tail.val) {
        if (this.length === 1) {
            popNode = this.head
            this.head = this.head.next
            this.tail = this.head
        } else {
            popNode = this.head
            this.head = this.head.next
            this.head.prev = null
        }
        this.length -= 1
        return popNode
    }
}

Queue.prototype.getQueue = function() {
    let queue = []
    let cur = this.head
    
    while (cur) {
        const item = cur.value
        queue.push(item)
        cur = cur.next
    }
    console.log(queue)
    return queue
}

let q = new Queue()
q.enQueue(1)
q.getQueue()
q.deQueue()
q.getQueue()
q.enQueue(1)
q.enQueue(2)
q.enQueue(3)
q.enQueue(4)
q.enQueue(5)
q.enQueue(6)
q.deQueue()
q.getQueue()
