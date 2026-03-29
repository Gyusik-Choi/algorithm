package com.example

class DesignCircularDeque641_3(k: Int) {
    var head: Node? = null
    var tail: Node? = null
    var curSize = 0
    val maxSize = k

    fun insertFront(value: Int): Boolean {
        val onInsert: (Node) -> Unit = { node ->
            val oldHead = head
            head = node
            head!!.next = oldHead
            oldHead!!.prev = head
        }
        return insert(value, onInsert)
    }

    fun insertLast(value: Int): Boolean {
        val onInsert: (Node) -> Unit = { node ->
            val oldTail = tail
            tail = node
            tail!!.prev = oldTail
            oldTail!!.next = tail
        }
        return insert(value, onInsert)
    }

    private fun insert(value: Int, onInsert: (Node) -> Unit): Boolean {
        if (isFull()) return false
        val node = Node(value)
        if (isEmpty()) {
            head = node
            tail = node
        } else {
            onInsert(node)
        }
        curSize += 1
        return true
    }

    fun deleteFront(): Boolean {
        val onDelete: () -> Unit = {
            val next = head!!.next
            head = next
            head!!.prev = null
        }
        return delete(onDelete)
    }

    fun deleteLast(): Boolean {
        val onDelete: () -> Unit = {
            val prev = tail!!.prev
            tail = prev
            tail!!.next = null
        }
        return delete(onDelete)
    }

    private fun delete(onDelete: () -> Unit): Boolean {
        if (isEmpty()) return false
        if (curSize == 1) {
            head = null
            tail = null
        } else {
            onDelete()
        }
        curSize -= 1
        return true
    }

    fun getFront(): Int {
        return if (isEmpty()) -1 else head!!.value
    }

    fun getRear(): Int {
        return if (isEmpty()) -1 else tail!!.value
    }

    fun isEmpty(): Boolean {
        return curSize == 0
    }

    fun isFull(): Boolean {
        return curSize == maxSize
    }

    class Node(k: Int) {
        var prev: Node? = null
        var next: Node? = null
        val value = k
    }
}
