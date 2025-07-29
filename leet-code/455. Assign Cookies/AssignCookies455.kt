package com.example

class AssignCookies455 {
    fun findContentChildren(g: IntArray, s: IntArray): Int {
        g.sort()
        s.sort()
        var maxNumber = 0
        var idx = 0
        for (size in s) {
            if (idx >= g.size) {
                break
            }
            if (size >= g[idx]) {
                maxNumber += 1
                idx += 1
            }
        }
        return maxNumber
    }
}
