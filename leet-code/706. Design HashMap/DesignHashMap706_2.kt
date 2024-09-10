class DesignHashMap706_2 {
    private val maxSize: Int = 1000001
    private val nodes: Array<Node?> = arrayOfNulls<Node>(maxSize)

    fun put(key: Int, value: Int) {
        val idx = getIdx(key)
        if (nodes[idx] == null) {
            nodes[idx] = Node(key, value)
            return
        }

        var node: Node? = nodes[idx]
        while (node != null) {
            if (node.key == key) {
                node.value = value
                return
            }
            node = node.next
        }
        node = Node(key, value)
    }

    fun get(key: Int): Int {
        val idx = getIdx(key)
        if (nodes[idx] == null) {
            return -1
        }

        var node: Node? = nodes[idx]
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
        if (nodes[idx] == null) {
            return
        }

        var node = nodes[idx]
        if (nodes[idx]!!.key == key) {
            if (nodes[idx]?.next == null) {
                nodes[idx] = null
            } else {
                nodes[idx] = node!!.next
            }
            return
        }


        var prev: Node? = nodes[idx]
        while (node != null) {
            if (node.key == key) {
                prev!!.next = node.next
                return
            }
            prev = node
            node = node.next
        }
    }

    private fun getIdx(key: Int): Int {
        return key % maxSize
    }

    private class Node(val key: Int, var value: Int) {
        var next: Node? = null
    }
}
