package com.example

import java.util.PriorityQueue

class ReconstructItinerary332 {
    fun findItinerary(tickets: List<List<String>>): List<String> {
        val map = mutableMapOf<String, PriorityQueue<String>>()
        tickets.forEach { ticket ->
            val start = ticket[0]
            val end = ticket[1]
            map.putIfAbsent(start, PriorityQueue())
            map[ticket[0]]!!.add(end)
        }
        val itinerary = mutableListOf<String>()
        dfs(map, itinerary, "JFK")
        return itinerary
    }

    private fun dfs(
        map: MutableMap<String, PriorityQueue<String>>,
        itinerary: MutableList<String>,
        departure: String,
    ) {
        while (map.contains(departure) && map[departure]!!.isNotEmpty()) {
            dfs(map, itinerary, map[departure]!!.poll())
        }
        itinerary.add(0, departure)
    }
}
