class DesignCircularQueue_3(k: Int) {
    val circularQ: IntArray = IntArray(k)
    val maxSize: Int = k
    var length: Int = 0;
    var front: Int = 0;
    var rear: Int = -1;

    fun enQueue(value: Int): Boolean {
        if (isFull()) {
            return false
        }
        length += 1
        rear = (rear + 1) % maxSize
        circularQ[rear] = value
        return true
    }

    fun deQueue(): Boolean {
        if (isEmpty()) {
            return false
        }
        length -= 1
        front = (front + 1) % maxSize
        return true
    }

    fun Front(): Int {
        if (isEmpty()) {
            return -1
        }
        return circularQ[front]
    }

    fun Rear(): Int {
        if (isEmpty()) {
            return -1
        }
        return circularQ[rear]
    }

    fun isEmpty(): Boolean {
        return length == 0;
    }

    fun isFull(): Boolean {
        return maxSize == length;
    }
}