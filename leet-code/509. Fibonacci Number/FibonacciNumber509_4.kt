package com.example

class FibonacciNumber509_4 {
    fun fib(n: Int): Int {
        val arr = IntArray(n + 1)
        if (n < 2) return n
        arr[1] = 1
        for (i in 2..n) arr[i] = arr[i - 1] + arr[i - 2]
        return arr[n]
    }
}
