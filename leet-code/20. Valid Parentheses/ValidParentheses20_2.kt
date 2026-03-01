package com.example

import java.util.LinkedList

class ValidParentheses20_2 {
    private val stack = LinkedList<Char>()
    private val map = hashMapOf('(' to ')','[' to ']','{' to '}')

    fun isValid(s: String): Boolean {
        for (c in s) {
            if (map.containsKey(c)) {
                stack.push(c)
            } else {
                if (stack.isEmpty() || !map.containsKey(stack.peek()) || map[stack.peek()] != c) {
                    return false
                }
                stack.pop()
            }
        }
        return stack.isEmpty()
    }
}
