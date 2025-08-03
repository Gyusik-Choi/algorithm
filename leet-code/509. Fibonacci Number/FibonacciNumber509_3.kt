package com.example

class FibonacciNumber509_3 {
    private val map = mutableMapOf(0 to 0, 1 to 1)

    fun fib(n: Int): Int {
        if (map.containsKey(n)) {
            return map[n]!!
        }
        map[n] = fib(n - 1) + fib(n - 2)
        return map[n]!!
    }
}
