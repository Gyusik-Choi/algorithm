package com.example

class Programmers92334 {
    fun solution(id_list: Array<String>, report: Array<String>, k: Int): IntArray {
        val reportMap = mutableMapOf<String, MutableSet<String>>()
        for (r in report) {
            val names = r.split(" ")
            val caller = names[0]
            val callee = names[1]
            val set = reportMap.getOrDefault(callee, mutableSetOf())
            set.add(caller)
            reportMap[callee] = set
        }

        val counts = mutableMapOf<String, Int>()
        for (value in reportMap.values) {
            if (value.size >= k) {
                for (reporter in value) {
                    counts[reporter] = counts.getOrDefault(reporter, 0) + 1
                }
            }
        }

        return id_list
            .map { x -> counts.getOrDefault(x, 0) }
            .toIntArray()
    }
}
