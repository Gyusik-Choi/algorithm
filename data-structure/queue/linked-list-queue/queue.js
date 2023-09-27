// https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Functions/Default_parameters

const Node = function(value, next = null) {
    this.value = value
    this.next = next
}

const Queue = function() {
    this.head = new Node(null)
    this.tail = this.head
}

Queue.prototype.isEmpty = function() {
    if (this.head.value === null) {
        return true
    }
    return false
}

Queue.prototype.enQueue = function(item) {
    if (this.isEmpty()) {
        this.head = new Node(item)
        this.tail = this.head
    } else {
        let cur = this.tail
        this.tail = new Node(item)
        cur.next = this.tail
    }
}

Queue.prototype.deQueue = function() {
    if (this.isEmpty()) {
        console.log("queue is empty")
        return
    } else {
        if (this.head === this.tail) {
            const number = this.head.value
            this.head = new Node(null)
            this.tail = this.head
        } else {
            this.head = this.head.next
        }
    }
}

Queue.prototype.getQueue = function() {
    let arr = []
    let cur = this.head

    if (!this.isEmpty()) {
        while (cur) {
            arr.push(cur.value)
            cur = cur.next
        }
    }
    console.log(arr)
    return arr
}

let q = new Queue()
q.enQueue(1)
q.getQueue()
q.deQueue()
q.getQueue()
// q.enQueue(1)
// q.enQueue(2)
// q.enQueue(3)
// q.enQueue(4)
// q.enQueue(5)
// q.enQueue(6)
// q.deQueue()
// q.getQueue()