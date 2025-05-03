package com.example.algorithm

import java.util.PriorityQueue

class Programmers43164 {
    fun solution(tickets: Array<Array<String>>): Array<String> {
        val map = mutableMapOf<String, PriorityQueue<String>>()
        for (ticket in tickets) {
            map.putIfAbsent(ticket[0], PriorityQueue<String>())
            map[ticket[0]]!!.add(ticket[1])
        }
        val history = mutableListOf<String>()
        dfs(map, history, "ICN")
        return history.toTypedArray()
    }

    private fun dfs(
        map: MutableMap<String, PriorityQueue<String>>,
        visit: MutableList<String>,
        departure: String,
    ) {
        while (map.containsKey(departure) && !map[departure]!!.isEmpty()) {
            val arrival = map[departure]!!.poll()
            dfs(map, visit, arrival)
        }
        visit.add(0, departure)
    }
}
