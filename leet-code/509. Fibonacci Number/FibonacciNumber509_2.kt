package com.example

class FibonacciNumber509_2 {
    private val map = mutableMapOf(0 to 0, 1 to 1)

    fun fib(n: Int): Int {
        if (map.containsKey(n)) {
            return map[n]!!
        }
        val num1 = fib(n - 1)
        val num2 = fib(n - 2)
        map[n - 1] = num1
        map[n - 2] = num2
        return num1 + num2
    }
}
