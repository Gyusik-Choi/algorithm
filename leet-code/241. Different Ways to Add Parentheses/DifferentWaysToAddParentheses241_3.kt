package com.example

class DifferentWaysToAddParentheses241_3 {
    fun diffWaysToCompute(expression: String): List<Int> {
        return diffWaysToCompute(expression, mutableListOf())
    }

    private fun diffWaysToCompute(expression: String, answer: MutableList<Int>): MutableList<Int> {
        if (expression.none { it in "+-*" }) return mutableListOf(expression.toInt())
        for (i in 0..expression.lastIndex) {
            val e = expression[i]
            if (e != '+' && e != '-' && e != '*') continue
            val left = diffWaysToCompute(expression.substring(0, i), mutableListOf())
            val right = diffWaysToCompute(expression.substring(i + 1), mutableListOf())
            for (l in left) {
                for (r in right) {
                    when (e) {
                        '+' -> answer.add(l + r)
                        '-' -> answer.add(l - r)
                        else -> answer.add(l * r)
                    }
                }
            }
        }
        return answer
    }
}
