class DesignCircularDeque641_2(k: Int) {
    private val maxSize: Int = k;
    private var length: Int = 0;
    private var head: DoublyLinkedList = DoublyLinkedList(-1)
    private var tail: DoublyLinkedList = DoublyLinkedList(-1)

    init {
        head.right = tail;
        tail.left = head;
    }

    fun insertFront(value: Int): Boolean {
        if (isFull())
            return false
        val node: DoublyLinkedList = DoublyLinkedList(value)
        node.left = head
        node.right = head.right
        head.right!!.left = node
        head.right = node
        length += 1
        return true
    }

    fun insertLast(value: Int): Boolean {
        if (isFull())
            return false
        val node: DoublyLinkedList = DoublyLinkedList(value)
        node.left = tail.left
        node.right = tail
        tail.left!!.right = node
        tail.left = node
        length += 1
        return true
    }

    fun deleteFront(): Boolean {
        if (isEmpty())
            return false
        head.right = head.right!!.right
        head.right!!.left = head
        length -= 1
        return true
    }

    fun deleteLast(): Boolean {
        if (isEmpty())
            return false
        tail.left = tail.left!!.left
        tail.left!!.right = tail
        length -= 1
        return true
    }

    fun getFront(): Int {
        return if (isEmpty()) -1 else head.right!!.value
    }

    fun getRear(): Int {
        return if (isEmpty()) -1 else tail.left!!.value
    }

    fun isEmpty(): Boolean {
        return length == 0
    }

    fun isFull(): Boolean {
        return maxSize == length
    }

    class DoublyLinkedList(val value: Int) {
        var left: DoublyLinkedList? = null;
        var right: DoublyLinkedList? = null;
    }
}
