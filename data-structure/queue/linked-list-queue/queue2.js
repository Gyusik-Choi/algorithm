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
        let tail = this.tail
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
        const popNode = this.head.value
        // length 프로퍼티를 추가해서 보다 명료하게 숫자가 1개만 있는 경우를 나타내도록 했다
        // if (this.head === this.tail) {
        if (this.length === 1) {
            this.head = this.head.next
            this.tail = this.head
        } else {
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
