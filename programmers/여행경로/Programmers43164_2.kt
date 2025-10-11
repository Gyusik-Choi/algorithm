package com.example

import java.util.LinkedList
import java.util.PriorityQueue

class Programmers43164_2 {
    fun solution(tickets: Array<Array<String>>): Array<String> {
        val map = mutableMapOf<String, PriorityQueue<String>>()
        tickets.forEach { ticket ->
            map.putIfAbsent(ticket[0], PriorityQueue<String>())
            map[ticket[0]]!!.add(ticket[1])
        }
        val course = LinkedList<String>()
        val stack = LinkedList<String>()
        stack.push("ICN")
        while (!stack.isEmpty()) {
            while (map.containsKey(stack.peekFirst()) && map[stack.peekFirst()]!!.isNotEmpty()) {
                stack.push(map[stack.peekFirst()]!!.poll())
            }
            course.add(0, stack.pop())
        }
        return course.toTypedArray()
    }
}
