package com.example

import java.util.LinkedList

class DailyTemperatures739_2 {
    fun dailyTemperatures(temperatures: IntArray): IntArray {
        val answer = IntArray(temperatures.size)
        val stack = LinkedList<Int>()
        temperatures.forEachIndexed { index, value ->
            while (stack.isNotEmpty() && temperatures[stack.peek()] < value) {
                val idx = stack.pop()
                answer[idx] = index - idx
            }
            stack.push(index)
        }
        return answer
    }
}
