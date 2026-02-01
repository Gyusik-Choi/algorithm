package com.example.algorithm

import java.util.LinkedList
import kotlin.math.min

class TrappingRainWater42_3 {
    fun trap(height: IntArray): Int {
        var sums = 0
        val stack = LinkedList<Int>()
        for (i in height.indices) {
            while (stack.isNotEmpty() && height[stack.peek()] < height[i]) {
                val prev = stack.pop()
                if (stack.isEmpty()) {
                    break
                }
                val distance = i - stack.peek() - 1
                val depth = min(height[stack.peek()], height[i]) - height[prev]
                sums += distance * depth
            }
            stack.push(i)
        }
        return sums
    }
}
