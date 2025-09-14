package com.example

import java.util.LinkedList

class ImplementQueueUsingStacks232 {
    val stack = LinkedList<Int>()
    val stackHelper = LinkedList<Int>()

    fun push(x: Int) {
        stack.push(x)
    }

    fun pop(): Int {
        while (!stack.isEmpty()) {
            stackHelper.push(stack.pop())
        }
        val item = stackHelper.pop()
        while (!stackHelper.isEmpty()) {
            stack.push(stackHelper.pop())
        }
        return item
    }

    fun peek(): Int {
        while (!stack.isEmpty()) {
            stackHelper.push(stack.pop())
        }
        val item = stackHelper.peek()
        while (!stackHelper.isEmpty()) {
            stack.push(stackHelper.pop())
        }
        return item
    }

    fun empty(): Boolean {
        return stack.isEmpty()
    }
}
