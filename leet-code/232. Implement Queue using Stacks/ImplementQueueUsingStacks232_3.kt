package com.example

import java.util.LinkedList

class ImplementQueueUsingStacks232_3 {
    private val stack = LinkedList<Int>()
    private val innerStack = LinkedList<Int>()

    fun push(x: Int) {
        while (stack.isNotEmpty()) {
            innerStack.push(stack.pop())
        }
        stack.push(x)
        while (innerStack.isNotEmpty()) {
            stack.push(innerStack.pop())
        }
    }

    fun pop(): Int {
        return stack.pop()
    }

    fun peek(): Int {
        val peekItem = stack.pop()
        stack.push(peekItem)
        return peekItem
    }

    fun empty(): Boolean {
        return stack.size < 1
    }
}
