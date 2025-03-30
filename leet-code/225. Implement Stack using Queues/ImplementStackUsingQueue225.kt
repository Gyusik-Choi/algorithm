package com.example.algorithm

class ImplementStackUsingQueue225 {
    private val stack = ArrayDeque<Int>()

    fun push(x: Int) {
        stack.add(x)
        for (i in 1..stack.lastIndex) {
            stack.add(stack.removeFirst())
        }
    }

    fun pop(): Int {
        return stack.removeFirst()
    }

    fun top(): Int {
        return stack.first()
    }

    fun empty(): Boolean {
        return stack.size == 0
    }
}