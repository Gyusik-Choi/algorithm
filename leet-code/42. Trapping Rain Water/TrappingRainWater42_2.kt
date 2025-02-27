package com.example

import kotlin.math.min

/**
 * LeetCode 에서는
 * val: Deque<int> = ArrayDeque()
 * Java 의 Deque, ArrayDeque 를 import 해서
 * 위와 같이 작성하면 에러가 발생한다
 * LeetCode 에서는 채점시 Java 의 library 를 사용하지 않고
 * Kotlin 의 standard library 를 사용하는 듯 하다
 * 그래서 구현시 Kotlin library 의 ArrayDeque 의 메소드를 사용했다 <br>
 * https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-array-deque
 */
class TrappingRainWater42_2 {
    fun trap(height: IntArray): Int {
        var trappingWater = 0
        val stack = ArrayDeque<Int>()
        for (i in height.indices) {
            while (!stack.isEmpty() && height[stack.last()] < height[i]) {
                val top = stack.removeLast()
                if (stack.isEmpty()) break
                // val width = i - top
                // 위의 코드는 안 된다
                // trap -> [4, 2, 0, 3, 2, 5]
                // top 이 3(height 에서 값으로 3)일때
                // stack 에 남은건 0(height 에서 값으로 4)이다
                // top 으로 접근하면 width 를 3에서 5사이를 구하게 되는데
                // 실제로 구해야할 width 는 0에서 5까지다
                val width = i - stack.last() - 1
                val depth = min(height[i], height[stack.last()]) - height[top]
                trappingWater += width * depth
            }
            stack.addLast(i)
        }
        return trappingWater
    }
}