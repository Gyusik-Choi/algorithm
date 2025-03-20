package com.example

class ValidParentheses20 {
    fun isValid(s: String): Boolean {
        val stack = ArrayDeque<Char>()
        val map = mapOf(
            ')' to '(',
            '}' to '{',
            ']' to '[')
        for (character in s) {
            // '(', '{', '['
            if (!map.containsKey(character)) {
                stack.addLast(character)
            // ')', '}', ']'
            } else {
                if (stack.isEmpty()) {
                    return false
                }
                if (map[character] != stack.removeLast()) {
                    return false
                }
            }
        }
        return stack.isEmpty()
    }
}
