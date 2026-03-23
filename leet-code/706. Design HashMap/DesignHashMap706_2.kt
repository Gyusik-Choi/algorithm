package com.example

class DesignHashMap706_2 {
    private val size = 100000
    private val arr = arrayOfNulls<Node>(size)

    fun put(key: Int, value: Int) {
        val idx = getIdx(key)
        if (arr[idx] == null) {
            arr[idx] = Node(key, value)
            return
        }
        var node = arr[idx]
        while (node!!.next != null) {
            if (node.key == key) {
                node.value = value
                return
            }
            node = node.next!!
        }
        if (node.key == key) {
            node.value = value
            return
        }
        node.next = Node(key, value)
    }

    fun get(key: Int): Int {
        val idx = getIdx(key)
        if (arr[idx] == null) {
            return -1
        }
        var node = arr[idx]
        while (node != null) {
            if (node.key == key) {
                return node.value
            }
            node = node.next
        }
        return -1
    }

    fun remove(key: Int) {
        val idx = getIdx(key)
        if (arr[idx] == null) {
            return
        }
        if (arr[idx]!!.key == key) {
            arr[idx] = arr[idx]!!.next
            return
        }
        var prev = arr[idx]!!
        var node = arr[idx]!!.next
        while (node != null) {
            val next = node.next
            if (node.key == key) {
                prev.next = next
                return
            }
            prev = node
            node = next
        }
    }

    private fun getIdx(key: Int): Int {
        return key.mod(size)
    }

    class Node(val key: Int, var value: Int) {
        var next: Node? = null
    }
}