package com.example

class DesignCircularQueue622_2(k: Int) {
    private var front: Node? = null
    private var rear: Node? = null
    private val maxSize = k
    private var curSize = 0

    fun enQueue(value: Int): Boolean {
        if (isFull()) {
            return false
        }
        val oldRear = rear
        val newRear = Node(value)
        oldRear?.next = newRear
        rear = newRear
        if (isEmpty()) {
            front = rear
        }
        curSize += 1
        return true
    }

    fun deQueue(): Boolean {
        if (isEmpty()) {
            return false
        }
        val next = front!!.next
        front = next
        rear!!.next = next
        curSize -= 1
        return true
    }

    fun Front(): Int {
        return if (isEmpty()) -1 else front!!.value
    }

    fun Rear(): Int {
        return if (isEmpty()) -1 else rear!!.value
    }

    fun isEmpty(): Boolean {
        return curSize == 0
    }

    fun isFull(): Boolean {
        return curSize == maxSize
    }

    private class Node(k: Int) {
        val value = k
        var next: Node? = null
    }
}
