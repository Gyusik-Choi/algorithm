package com.example

class MergeIntervals56_2 {
    fun merge(intervals: Array<IntArray>): Array<IntArray> {
        val sortedIntervals = intervals.sortedArrayWith { a, b -> if (a[0] == b[0]) a[1] - b[1] else a[0] - b[0] }
        val list = mutableListOf<IntArray>()
        for (interval in sortedIntervals) {
            if (list.isEmpty() || list.last()[1] < interval[0]) {
                list.add(interval)
                continue
            }
            if (list.last()[1] < interval[1]) {
                list.last()[1] = interval[1]
            }
        }
        return list.toTypedArray()
    }
}
