package com.example

class DifferentWaysToAddParentheses241_2 {
    private val memo = mutableMapOf<String, List<Int>>()

    fun diffWaysToCompute(expression: String): List<Int> {
        if (memo.containsKey(expression)) {
            return memo[expression]!!
        }
        val result = mutableListOf<Int>()
        for (i in expression.indices) {
            if (expression[i] in "+-*") {
                val left = diffWaysToCompute(expression.substring(0, i))
                val right = diffWaysToCompute(expression.substring(i + 1, expression.length))
                for (l in left) {
                    for (r in right) {
                        when (expression[i]) {
                            '+' -> result.add(l + r)
                            '-' -> result.add(l - r)
                            '*' -> result.add(l * r)
                        }
                    }
                }
            }
        }
        if (result.isEmpty()) {
            result.add(expression.toInt())
        }
        memo[expression] = result
        return result
    }
}
