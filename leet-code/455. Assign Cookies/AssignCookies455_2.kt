package com.example

class AssignCookies455_2 {
    fun findContentChildren(g: IntArray, s: IntArray): Int {
        g.sort()
        s.sort()
        var contentSum = 0
        var gIdx = 0
        for (cookie in s) {
            if (gIdx == g.size) {
                break
            }
            if (g[gIdx] > cookie) {
                continue
            }
            contentSum += 1
            gIdx += 1
        }
        return contentSum
    }
}
