package com.example.algorithm

import java.util.LinkedList

class RemoveDuplicateLetters316_4 {
    fun removeDuplicateLetters(s: String): String {
        val counter = mutableMapOf<Char, Int>()
        val existsInStack = mutableMapOf<Char, Boolean>()
        val stack = LinkedList<Char>()
        for (c in s) {
            counter[c] = counter.getOrDefault(c, 0) + 1
            existsInStack[c] = false
        }
        for (c in s) {
            counter[c] = counter.getOrDefault(c, 0) - 1
            if (existsInStack[c] == true) {
                continue
            }
            while (stack.isNotEmpty() && stack.peek() > c && counter[stack.peek()]!! > 0) {
                existsInStack[stack.pop()] = false
            }
            existsInStack[c] = true
            stack.push(c)
        }
        val sb = StringBuilder()
        while (stack.isNotEmpty()) {
            sb.append(stack.pop())
        }
        return sb.reverse().toString()
    }
}
