package com.example

class MinimumHeightTrees310_2 {
    fun findMinHeightTrees(n: Int, edges: Array<IntArray>): List<Int> {
        if (n == 1) return listOf(0)
        val map = mutableMapOf<Int, MutableList<Int>>()
        val level = mutableMapOf<Int, Int>()
        for (edge in edges) {
            map.putIfAbsent(edge.first(), mutableListOf())
            map.putIfAbsent(edge.last(), mutableListOf())
            map[edge.first()]!!.add(edge.last())
            map[edge.last()]!!.add(edge.first())
            level[edge.first()] = level.getOrDefault(edge.first(), 0) + 1
            level[edge.last()] = level.getOrDefault(edge.last(), 0) + 1
        }
        while (level.size > 2) {
            val startList = findStartList(level)
            for (start in startList) {
                level.remove(start)
                if (!map.containsKey(start)) {
                    continue
                }
                for (end in map[start]!!) {
                    if (!level.containsKey(end)) {
                        continue
                    }
                    level[end] = level[end]!! - 1
                }
            }
        }
        return level.keys.toList()
    }

    private fun findStartList(levels: Map<Int, Int>): List<Int> {
        return levels.entries
            .filter { entry -> entry.value == 1 }
            .map { entry -> entry.key }
            .toList()
    }
}
