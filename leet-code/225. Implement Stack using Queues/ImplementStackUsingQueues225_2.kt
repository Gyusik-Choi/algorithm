package com.example

class ImplementStackUsingQueues225_2 {
    val queue = ArrayDeque<Int>()

    fun push(x: Int) {
        val list = mutableListOf<Int>()
        while (queue.isNotEmpty()) {
            list.add(queue.removeFirst())
        }
        queue.add(x)
        queue.addAll(list)
    }

    fun pop(): Int {
        return queue.removeFirst()
    }

    fun top(): Int {
        return queue.first()
    }

    fun empty(): Boolean {
        return queue.size == 0
    }
}

