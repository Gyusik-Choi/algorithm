package com.example

class Programmers92334_3 {
    fun solution(id_list: Array<String>, report: Array<String>, k: Int): IntArray {
        val reportee = mutableMapOf<String, MutableSet<String>>()
        for (r in report) {
            val users = r.split(" ")
            reportee.getOrPut(users[1]) { mutableSetOf() }.add(users[0])
        }
        val reporter = mutableMapOf<String, Int>()
        for (r in reportee) {
            if (r.value.size >= k) {
                for (v in r.value) {
                    reporter[v] = reporter.getOrDefault(v, 0) + 1
                }
            }
        }
        return id_list
            .map { reporter.getOrDefault(it, 0) }
            .toIntArray()
    }
}
