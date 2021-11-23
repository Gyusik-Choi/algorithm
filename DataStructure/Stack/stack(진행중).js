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
console.log(s)
s.add(2)
console.log(s)
s.remove()
console.log(s)
s.add(2)
s.add(3)
s.add(4)
s.add(5)
s.getStack()