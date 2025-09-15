package com.example

import java.util.LinkedList

class ImplementQueueUsingStacks232_2 {
    val input = LinkedList<Int>()
    val output = LinkedList<Int>()

    fun push(x: Int) {
        input.push(x)
    }

    fun pop(): Int {
        peek()
        return output.pop()
    }

    // output 이 비어있지 않다면
    // input 에 있는 요소를 output 으로 옮기지 않고
    // output 에서 바로 꺼낸다
    // output 이 비어있지 않은 사이
    // push 가 발생하면 input 에 그대로 쌓이게 된다
    // output 에는 기존에 input 에 들어온 요소를
    // 보관하고 있다가 빌 때까지 input 에 있는 요소를
    // output 에 옮길 필요없이 바로 output 에서 꺼낼 수 있다
    // output 에 있는 요소는 input 에 있는 요소보다
    // 이전에 들어온 요소만 남아있다
    fun peek(): Int {
        if (output.isEmpty()) {
            while (!input.isEmpty()) {
                output.push(input.pop())
            }
        }
        return output.peek()
    }

    fun empty(): Boolean {
        return input.isEmpty() && output.isEmpty()
    }
}
