package com.example

class MinimumHeightTrees310 {
    fun findMinHeightTrees(n: Int, edges: Array<IntArray>): List<Int> {
        if (edges.isEmpty()) {
            return listOf(0)
        }
        val map = mutableMapOf<Int, MutableList<Int>>()
        edges.forEach { edge ->
            map.putIfAbsent(edge[0], mutableListOf())
            map.putIfAbsent(edge[1], mutableListOf())
            map[edge[0]]!!.add(edge[1])
            map[edge[1]]!!.add(edge[0])
        }
        val lastRemoved = mutableListOf<Int>()
        while (map.keys.size > 2) {
            // 현재 values 에서 lastRemoved 에 있는 요소들 제거
            map.values.forEach { value -> value.removeAll { lastRemoved.contains(it) } }
            // values 의 길이가 1 이하인 key 제거
            val keyToRemove = map.entries.filter { it.value.size <= 1 }.map { it.key }
            lastRemoved.clear()
            for (k in keyToRemove) {
                map.remove(k)
                lastRemoved.add(k)
            }
        }
        return map.keys.toList()
    }
}
