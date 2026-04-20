package com.example

import java.util.*

class ReconstructItinerary332_2 {
    fun findItinerary(tickets: List<List<String>>): List<String> {
        val map = mutableMapOf<String, PriorityQueue<String>>()
        for (ticket in tickets) {
            map.putIfAbsent(ticket[0], PriorityQueue<String>())
            map[ticket[0]]!!.add(ticket[1])
        }
        return traverse(map, mutableListOf(), "JFK")
    }

    private fun traverse(
        route: MutableMap<String, PriorityQueue<String>>,
        itinerary: MutableList<String>,
        departure: String
    ): List<String> {
        while (route.containsKey(departure) && route[departure]!!.isNotEmpty()) {
            traverse(route, itinerary, route[departure]!!.poll())
        }
        itinerary.add(0, departure)
        return itinerary
    }
}
